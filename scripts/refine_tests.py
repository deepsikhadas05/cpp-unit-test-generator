import os
import subprocess
import yaml

REFINE_YAML = "../yaml_prompts/refine_tests.yaml"
TESTS_DIR = "../tests"
OLLAMA_MODEL = "phi"

def load_yaml(path):
    with open(path, 'r') as f:
        return yaml.safe_load(f)

def read_test_files(test_dir):
    test_data = ""
    for file in os.listdir(test_dir):
        if file.endswith(".cpp"):
            path = os.path.join(test_dir, file)
            with open(path, 'r') as f:
                test_data += f"\n\n// File: {file}\n" + f.read()
    return test_data

def refine_tests(prompt_yaml, code):
    prompt = yaml.dump(prompt_yaml)
    full_input = f"""### Instruction (YAML Prompt)
{prompt}

### C++ Unit Tests
{code}
"""
    print("🤖 Sending refined test prompt to Ollama...")
    result = subprocess.run(["ollama", "run", OLLAMA_MODEL], input=full_input, capture_output=True, text=True)
    return result.stdout

def write_refined_tests(response, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    parts = response.split("// File: ")
    for i, part in enumerate(parts[1:], 1):
        lines = part.split("\n", 1)
        filename = lines[0].strip()
        content = lines[1] if len(lines) > 1 else ""
        path = os.path.join(output_dir, filename)
        with open(path, 'w') as f:
            f.write(content)
    print("✅ Refined tests saved to:", output_dir)

def main():
    print("🛠️  Refining tests...")
    prompt_yaml = load_yaml(REFINE_YAML)
    tests = read_test_files(TESTS_DIR)
    refined_output = refine_tests(prompt_yaml, tests)
    write_refined_tests(refined_output, TESTS_DIR)

if __name__ == "__main__":
    main()
