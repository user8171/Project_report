.PHONY: git_push

git_push:
	git add .
	git commit -m 'Push'
	git rm --cached Makefile
	git rm --cached -r __pycache__
	git rm --cached -r .vs
	git push https://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@github.com/user8171/Project_report.git

