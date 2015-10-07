find ./data -name NOTES | xargs rm
mkdir cleaned_data
mv ./data/*/* ./cleaned_data/
for FILENAME in ./cleaned_data/; do mv $FILENAME $FILENAME.txt; done
