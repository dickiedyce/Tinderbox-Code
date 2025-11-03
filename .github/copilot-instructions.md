# Tinderbox Action Code Workspace

This workspace is designed for developing Tinderbox action code, automation scripts, and related tools.

## Project Focus
- Tinderbox action development using the Tinderbox action code language
- Automation script creation for validation and testing
- Code organization and testing workflows
- Action code documentation and examples

## Development Guidelines
- Follow Tinderbox action code conventions and syntax
- **CRITICAL: Use single quotes for Rule attributes, double quotes for string literals inside rules**
- Test actions before deployment using the validation script
- Document action parameters, usage, and expected behavior
- Organize code by functionality using descriptive filenames
- Use the provided template for new actions

## String Escaping Rules
⚠️ **Tinderbox has specific requirements for string quoting that must be followed:**

### Rule Attributes
```tinderbox
// ✅ CORRECT - Always use single quotes for Rule wrapper
$Rule("/Prototypes/pStory") = 'if($Status == "Ready") { $Color="#00FF00"; }';

// ❌ WRONG - Double quotes cause rule truncation in Tinderbox  
$Rule("/Prototypes/pStory") = "if($Status == \"Ready\") { $Color=\"#00FF00\"; }";
```

### Prototype Assignment (CRITICAL)
**MUST be the absolute first line in any OnAdd function:**
```tinderbox
// ✅ CORRECT - KeyAttributes reset is first line
function buildProject() {
   $KeyAttributes=;$Prototype="pProject";
   logMessage("Building: " + $Name);
}

// ❌ WRONG - Any code before KeyAttributes prevents assignment
function buildProject() {
   logMessage("Building: " + $Name);
   $KeyAttributes=;$Prototype="pProject";
}
```

### Validation
- The build script automatically validates string escaping
- Run `python builder/build.py --validate` to check definitions
- Rules are validated before installer generation

## Workspace Structure
- `/actions/` - Main action code files (.txt format)
- `/scripts/` - Shell scripts for validation and automation
- `/examples/` - Sample action implementations for learning
- `/docs/` - Documentation, references, and testing guides
- `/tests/` - Test data and validation resources

## Getting Started
1. Use `actions/template.txt` as starting point for new actions
2. Validate code with `./scripts/validate-action.sh <file>`
3. Test actions in Tinderbox with sample data from `/tests/`
4. Document new patterns in `/examples/` directory

## VS Code Tasks
- "Validate Template Action" - Runs validation on the template file
- Use Command Palette (Cmd+Shift+P) -> "Tasks: Run Task" to execute