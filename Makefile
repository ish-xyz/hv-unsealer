.PHONY:	all

backendImage 	= "consulmod"
backendName  	= "consulmod"
networkName  	= "vault-autounsealing"
moduleImage		= "vaultmod"
moduleName		= "vaultmod"

infraBuild:
	docker network create ${networkName}

platformBuild:
	docker build -t ${backendImage} -f tests/platform/consul/Dockerfile.online tests/platform/consul/
	docker run --network ${networkName} -p 8500:8500 -td --name ${backendName} ${backendImage}
	docker build -t ${moduleImage} -f tests/platform/vault/Dockerfile.online tests/platform/vault/
	docker run --network ${networkName} -td --cap-add IPC_LOCK --name ${moduleName} ${moduleImage}

import:
	docker cp . ${moduleName}:/mnt/

cleanup:
	docker rm -f ${backendName}
	docker rm -f ${moduleName}
	docker rmi ${backendImage} ${moduleImage}
	docker network rm ${networkName}

testModule:
	docker exec -t ${moduleName} bash -c "cd /mnt/tests/modules && python consulTests.py"
	docker exec -t ${moduleName} bash -c "cd /mnt/tests/modules && python vaultTests.py"
	docker exec -t ${moduleName} bash -c "cd /mnt/tests/modules && python baseTests.py"
	docker exec -t ${moduleName} bash -c "cd /mnt/tests/modules && python secretslibTests.py"

localTest: infraBuild platformBuild import testModule
