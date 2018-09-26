.PHONY:	all

backendImage 	= "consulmod"
backendName  	= "consulmod"
networkName  	= "vault-autounsealing"
moduleImage		= "vaultmod"
moduleName		= "vaultmod"

infraBuild:
	docker network create ${networkName}

platformBuild: infraBuild
	docker build -t ${backendImage} -f tests/platform/consul/Dockerfile.online tests/platform/consul/
	docker run --network ${networkName} -td --name ${backendName} ${backendImage}
	docker build -t ${moduleImage} -f tests/platform/vault/Dockerfile.online tests/platform/vault/
	docker run --network ${networkName} -td --name ${moduleName} ${moduleImage}

import:
	docker cp . ${moduleName}:/mnt/

cleanup:
	docker rm -f ${backendName}
	docker rm -f ${moduleName}
	docker rmi ${backendImage} ${moduleImage}
	docker network rm ${networkName}

testModule:
	docker logs ${moduleName}
	docker logs ${backendName}
	docker exec -t ${moduleName} bash -c "cd /mnt/tests/modules && python consulTests.py"
	docker exec -t ${moduleName} bash -c "cd /mnt/tests/modules && python vaultTests.py"