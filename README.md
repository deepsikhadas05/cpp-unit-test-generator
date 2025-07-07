# 🧪 C++ Unit Test Generator for orgChartApi

This project implements a unit test generation pipeline using an LLM (Ollama) for the [`orgChartApi`](https://github.com/keploy/orgChartApi) C++ application. It automatically generates and refines Google Test-based unit tests, compiles them, and measures code coverage.

---

## 🚀 Project Structure

cpp-unit-test-generator/
├── orgChartApi/ # Cloned orgChartApi C++ source project
├── tests/ # LLM-generated unit tests (test_*.cpp)
├── yaml_prompts/ # YAML instructions for test generation and refinement
├── scripts/ # Automation scripts to interact with LLM
├── build/ # CMake build files and compiled test binaries
└── report.md # Summary of approach and coverage results

markdown
Copy
Edit

---

## 🧠 LLM Integration (Ollama)

We use a local LLM (e.g., `phi` or `llama3`) via [Ollama](https://ollama.com) to:
- Generate unit tests (`generate_tests.py`)
- Refine and deduplicate tests (`refine_tests.py`)
- Improve code coverage iteratively

---

## 📜 Instructions

### 1. Setup

Make sure you have the following:
- `g++`, `cmake`, and `make`
- [Google Test](https://github.com/google/googletest)
- [Ollama](https://ollama.com) with a supported model (e.g., `phi`)

### 2. Generate Tests

```bash
python scripts/generate_tests.py
3. Refine Tests
bash
Copy
Edit
python scripts/refine_tests.py
4. Build & Run Tests
From Ubuntu or MSVC environment:

bash
Copy
Edit
mkdir build && cd build
cmake ..
make
./runTests
5. Coverage Report (Optional)
bash
Copy
Edit
lcov --capture --directory . --output-file coverage.info
genhtml coverage.info --output-directory coverage_report
✅ Deliverables
✅ tests/ folder with final test cases

✅ YAML prompt files for repeatability

✅ CI-ready build using CMakeLists.txt

✅ report.md describing the coverage achieved

📊 Sample Output
🎯 Total Tests Generated: N
✅ Pass Rate: 100%
📈 Coverage: Coming soon (via lcov or OpenCppCoverage)

🛠️ Future Improvements
Fine-tune LLM prompts for higher assertion quality

Add GitHub Actions to automate test runs

Integrate with code review tools for test suggestions

🤝 Acknowledgements
Keploy for the base C++ project

Ollama for running local LLMs

Google Test for test framework

