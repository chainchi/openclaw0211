#!/bin/bash
CONTENT=$(cat fvt_report_2026.html | jq -sR .)
curl -X POST https://api.github.com/gists \
  -H "Content-Type: application/json" \
  -d "{\"public\":true,\"files\":{\"fvt_report_2026.html\":{\"content\":$CONTENT}}}"
