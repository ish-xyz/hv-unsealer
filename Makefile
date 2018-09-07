.PHONY:	all

backendImage 	= "ube"
backendName  	= "cube"
networkName  	= "vault-unsealing"
moduleImage	= "vufe"
moduleName	= "vault-unsealing"

infraBuild:
	docker network create ${networkName}

platformBuild: infraBuild
	docker build -t ${backendImage} -f tests/platform/backend/Dockerfile.offline tests/platform/backend/
	docker run --network ${networkName} -td -p 8500:8500 --name ${backendName} ${backendImage}
	docker build -t ${moduleImage} -f tests/platform/frontend/Dockerfile.offline tests/platform/frontend/
	docker run --network ${networkName} -v $$(pwd):/mnt -td --name ${moduleName} ${moduleImage}  

cleanup:
	docker rm -f ${backendName}
	docker rm -f ${moduleName}
	docker network rm ${networkName}
