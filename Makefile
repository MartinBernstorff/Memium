.DEFAULT_GOAL := help
.PHONY: coverage deps help lint publish push test tox
help: 
	@echo "This project uses Invoke (pyinvoke.org) for task management."
	@echo Install it via 
	@echo 
	@echo "     pip install invoke"
	@echo
	@echo and then run 
	@echo 
	@echo "     inv --list"
	@echo 
	@echo to get available tasks.