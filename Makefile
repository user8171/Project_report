.PHONY: git_push

git_push:
	git add .
	git commit -m 'Push'
	git rm --cached Makefile
	git rm --cached -r __pycache__
	git rm --cached -r .vs
	git push https://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@github.com/user8171/Project_report.git

