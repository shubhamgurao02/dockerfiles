repo=https://nexus-prod.ncl.com/repository/helm-charts/
chart_name=$(shell sed -En 's/^name:[[:space:]]+//p' Chart.yaml)
version=$(shell sed -En 's/^version:[[:space:]]+//p' Chart.yaml)

add:
	helm repo add nclh $(repo)
registry:
	helm registry login $(repo)
install-plugs:
	helm plugin install https://github.com/karuppiah7890/helm-schema-gen.git
values-schema:
	helm schema-gen values.yaml > values.schema.json
repo-list:
	helm repo list
repo-add:
	helm repo add \
		- username <your_github_username>
		- password <your_github_token>
 		my-github-helm-repo 'https://raw.githubusercontent.com/my_organization/my-github-helm-repo/master/'
chart-data:
	@echo $(chart_name)
	@echo $(version)
package:
	helm dependency update
	helm package . -d releases
index:
	helm repo index releases
publish:
	helm chart push $(repo)/$(chart_name):$(version)
push:
	curl -u ${NEXUS_USER}:${NEXUS_PASS} $(repo) --upload-file releases/$(chart_name)-$(version).tgz -v
