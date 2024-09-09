OUTPUT_FILE="AUTHORS"


contributors=$(curl -s -X GET "$REPO_URL")


echo "# List of contributors to the AirBnB Clone project" > $OUTPUT_FILE
echo "" >> $OUTPUT_FILE
for contributor in $(echo "$contributors" | jq -r '.[] | .login'); do
  echo "* $contributor" >> $OUTPUT_FILE
done
