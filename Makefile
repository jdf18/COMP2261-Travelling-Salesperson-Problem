USERNAME=ssqf78

PROFORMA_NAME=AISearchProforma
PROFORMA_PDF=export/$(PROFORMA_NAME).pdf

clean_submission:
	rm -rf $(USERNAME)

generate_proforma:
	echo "Generating proforma PDF"
	soffice --headless --convert-to pdf $(PROFORMA_NAME).docx --outdir export

run_all:
	python3 hasher.py run them anyway

final_res: run_all
	rm -rf final_results/*
	python3 find_best.py

submission_folder: clean_submission generate_proforma final_res
	echo "Creating submission folder"
	mkdir -p $(USERNAME)
	cp algorithms/Alg*.py $(USERNAME)
	cp final_results/* $(USERNAME)
	cp $(PROFORMA_PDF) $(USERNAME)

validation: submission_folder
	python3 validate_before_handin.py
	mv AISearchValidationFeedback.txt $(USERNAME)
	# Revalidate now the validation feedback is in the correct place
	python3 validate_before_handin.py
	mv AISearchValidationFeedback.txt $(USERNAME)
	less $(USERNAME)/AISearchValidationFeedback.txt

zip: validation
	rm $(USERNAME).zip
	zip -r $(USERNAME).zip $(USERNAME)/

