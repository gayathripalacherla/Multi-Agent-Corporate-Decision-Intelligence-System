from workflows.decision_workflow import run_decision_workflow

def main():
    proposal = "Should the company launch an AI-powered customer support assistant within the next quarter?"
    result = run_decision_workflow(proposal)
    print(result)

if __name__ == "__main__":
    main()
