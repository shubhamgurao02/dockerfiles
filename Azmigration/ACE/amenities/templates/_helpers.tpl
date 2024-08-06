{{/*
Expand the name of the chart.
*/}}
{{- define "amenities.name" -}}
{{- default .Chart.Name .Values.nameOverride | trunc 63 | trimSuffix "-" }}
{{- end }}

{{/*
Create a default fully qualified app name.
We truncate at 63 chars because some Kubernetes name fields are limited to this (by the DNS naming spec).
If release name contains chart name it will be used as a full name.
*/}}
{{- define "amenities.fullname" -}}
{{- if .Values.fullnameOverride }}
{{- .Values.fullnameOverride | trunc 63 | trimSuffix "-" }}
{{- else }}
{{- $name := default .Chart.Name .Values.nameOverride }}
{{- if contains $name .Release.Name }}
{{- .Release.Name | trunc 63 | trimSuffix "-" }}
{{- else }}
{{- printf "%s-%s" .Release.Name $name | trunc 63 | trimSuffix "-" }}
{{- end }}
{{- end }}
{{- end }}

{{/*
Create config names
*/}}
{{- define "amenities.cnfg.gen" -}}
{{- default .Chart.Name .Values.nameConfigGeneric | trunc 63 | trimSuffix "-" }}
{{- end }}

{{- define "amenities.cnfg.barauth" -}}
{{- default .Chart.Name .Values.nameConfigBarAuth | trunc 63 | trimSuffix "-" }}
{{- end }}

{{- define "amenities.cnfg.ts" -}}
{{- default .Chart.Name .Values.nameConfigTrustStore | trunc 63 | trimSuffix "-" }}
{{- end }}

{{- define "amenities.cnfg.dbparm" -}}
{{- default .Chart.Name .Values.nameConfigDbParam | trunc 63 | trimSuffix "-" }}
{{- end }}

{{- define "amenities.cnfg.servercon" -}}
{{- default .Chart.Name .Values.nameConfigServerConfig | trunc 63 | trimSuffix "-" }}
{{- end }}

{{- define "amenities.cnfg.policyprj" -}}
{{- default .Chart.Name .Values.nameConfigPolicyProject | trunc 63 | trimSuffix "-" }}
{{- end }}

{{- define "amenities.cnfg.odbcini" -}}
{{- default .Chart.Name .Values.nameConfigOdbcIni | trunc 63 | trimSuffix "-" }}
{{- end }}
{{/*
Create chart name and version as used by the chart label.
*/}}
{{- define "amenities.chart" -}}
{{- printf "%s-%s" .Chart.Name .Chart.Version | replace "+" "_" | trunc 63 | trimSuffix "-" }}
{{- end }}

{{/*
Common labels
*/}}
{{- define "amenities.labels" -}}
helm.sh/chart: {{ include "amenities.chart" . }}
{{ include "amenities.selectorLabels" . }}
{{- if .Chart.AppVersion }}
app.kubernetes.io/version: {{ .Chart.AppVersion | quote }}
{{- end }}
app.kubernetes.io/managed-by: {{ .Release.Service }}
{{- end }}

{{/*
Selector labels
*/}}
{{- define "amenities.selectorLabels" -}}
app.kubernetes.io/name: {{ include "amenities.name" . }}
app.kubernetes.io/instance: {{ .Release.Name }}
{{- end }}

{{/*
Create the name of the service account to use
*/}}
{{- define "amenities.serviceAccountName" -}}
{{- if .Values.serviceAccount.create }}
{{- default (include "amenities.fullname" .) .Values.serviceAccount.name }}
{{- else }}
{{- default "default" .Values.serviceAccount.name }}
{{- end }}
{{- end }}
