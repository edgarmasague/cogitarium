BACKEND_DIR=backend

run:
	@echo "Starting FastAPI server..."
	cd $(BACKEND_DIR) && uvicorn main:app --reload

cli:
	@echo "Launching AI Assistant in terminal mode..."
	cd $(BACKEND_DIR) && python cli.py

install:
	@echo "Installing dependencies..."
	cd $(BACKEND_DIR) && pip install -r requirements.txt

format:
	@echo "Formatting code with black..."
	cd $(BACKEND_DIR) && black .

lint:
	@echo "Linting code with flake8..."
	cd $(BACKEND_DIR) && flake8 .

clean:
	@echo "Cleaning pycache files..."
	cd $(BACKEND_DIR) && find . -type d -name "__pycache__" -exec rm -r {} +
	cd $(BACKEND_DIR) && rm -rf cache/*
	cd $(BACKEND_DIR) && rm -rf logs/*


help:
	@echo "Available commands:"
	@echo "  make run     - Run FastAPI server"
	@echo "  make cli     - Run assistant in terminal mode"
	@echo "  make install - Install dependencies"
	@echo "  make format  - Format code using Black"
	@echo "  make lint    - Lint code using flake8"
	@echo "  make clean   - Remove __pycache__ folders"
