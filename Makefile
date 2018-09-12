.PHONY:	all

backendImage 	= "consulmod"
backendName  	= "consulmod"
networkName  	= "vault-autounsealing"
moduleImage		= "vaultmod"
moduleName		= "vaultmod"

infraBuild:
	docker network create ${networkName}

platformBuild: infraBuild
	docker build -t ${backendImage} -f tests/platform/consul/Dockerfile.offline tests/platform/consul/
	docker run --network ${networkName} -td -p 8500:8500 --name ${backendName} ${backendImage}
	docker build -t ${moduleImage} -f tests/platform/vault/Dockerfile.offline tests/platform/vault/
	docker run --network ${networkName} -v $$(pwd):/mnt -td -p 8125:8125 -p 8200:8200 --name ${moduleName} ${moduleImage}  

cleanup:
	docker rm -f ${backendName}
	docker rm -f ${moduleName}
	docker rmi ${backendImage} ${moduleImage}
	docker network rm ${networkName}
