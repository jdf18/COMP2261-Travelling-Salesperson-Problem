USERNAME=ssqf78

PROFORMA_NAME=AISearchProforma
PROFORMA_PDF=export/$(PROFORMA_NAME).pdf

clean_submission:
	rm -rf $(USERNAME)

generate_proforma:
	echo "Generating proforma PDF"
	soffice --headless --convert-to pdf $(PROFORMA_NAME).docx --outdir export

submission_folder: clean_submission generate_proforma
	echo "Creating submission folder"
	mkdir -p $(USERNAME)
	cp algorithms/* $(USERNAME)
	cp $(PROFORMA_PDF) $(USERNAME)

validation: submission_folder
	python3 validate_before_handin.py
	mv AISearchValidationFeedback.txt $(USERNAME)

