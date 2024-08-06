{{/*
Expand the name of the chart.
*/}}
{{- define "oms.name" -}}
{{- default .Chart.Name .Values.nameOverride | trunc 63 | trimSuffix "-" }}
{{- end }}

{{/*
Create a default fully qualified app name.
We truncate at 63 chars because some Kubernetes name fields are limited to this (by the DNS naming spec).
If release name contains chart name it will be used as a full name.
*/}}
{{- define "oms.fullname" -}}
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
{{- define "oms.cnfg.gen" -}}
{{- default .Chart.Name .Values.nameConfigGeneric | trunc 63 | trimSuffix "-" }}
{{- end }}

{{- define "oms.cnfg.barauth" -}}
{{- default .Chart.Name .Values.nameConfigBarAuth | trunc 63 | trimSuffix "-" }}
{{- end }}

{{- define "oms.cnfg.ts" -}}
{{- default .Chart.Name .Values.nameConfigTrustStore | trunc 63 | trimSuffix "-" }}
{{- end }}

{{- define "oms.cnfg.dbparm" -}}
{{- default .Chart.Name .Values.nameConfigDbParam | trunc 63 | trimSuffix "-" }}
{{- end }}

{{- define "oms.cnfg.servercon" -}}
{{- default .Chart.Name .Values.nameConfigServerConfig | trunc 63 | trimSuffix "-" }}
{{- end }}

{{- define "oms.cnfg.policyprj" -}}
{{- default .Chart.Name .Values.nameConfigPolicyProject | trunc 63 | trimSuffix "-" }}
{{- end }}

{{- define "oms.cnfg.odbcini" -}}
{{- default .Chart.Name .Values.nameConfigOdbcIni | trunc 63 | trimSuffix "-" }}
{{- end }}

{{/*
Create chart name and version as used by the chart label.
*/}}
{{- define "oms.chart" -}}
{{- printf "%s-%s" .Chart.Name .Chart.Version | replace "+" "_" | trunc 63 | trimSuffix "-" }}
{{- end }}

{{/*
Common labels
*/}}
{{- define "oms.labels" -}}
helm.sh/chart: {{ include "oms.chart" . }}
{{ include "oms.selectorLabels" . }}
{{- if .Chart.AppVersion }}
app.kubernetes.io/version: {{ .Chart.AppVersion | quote }}
{{- end }}
app.kubernetes.io/managed-by: {{ .Release.Service }}
{{- end }}

{{/*
Selector labels
*/}}
{{- define "oms.selectorLabels" -}}
app.kubernetes.io/name: {{ include "oms.name" . }}
app.kubernetes.io/instance: {{ .Release.Name }}
{{- end }}

{{/*
Create the name of the service account to use
*/}}
{{- define "oms.serviceAccountName" -}}
{{- if .Values.serviceAccount.create }}
{{- default (include "oms.fullname" .) .Values.serviceAccount.name }}
{{- else }}
{{- default "default" .Values.serviceAccount.name }}
{{- end }}
{{- end }}
