.PHONY: git_push

git_push:
	git add .
	git commit -m 'Push'
	git rm --cached Makefile
	git rm --cached -r __pycache__
	git rm --cached -r .vs
	git push https://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@github.com/user8171/Project_report.git

