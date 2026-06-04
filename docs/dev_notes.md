To run backend:
    python back_end/app.py
To run frontend:
    cd front end
    npm run dev

VS Code run button may use wrong interpreter.
    Use terminal:
    conda activate jobmatch2
    python tests/test_data.py

Resolve path issues before read data file
    in app.py: 
    DATA_DIR / "file name" (if in data folder)

Backend Architecture Notes
- Refactored backend into modular pipeline structure.
- Switched internal src imports to relative imports for maintainability.
- Use module execution (python -m src.pipeline) for testing to avoid import path issues.