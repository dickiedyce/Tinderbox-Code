#!/bin/bash

# Tinderbox Action Validator Script
# This script helps validate action code syntax and common issues

echo "Tinderbox Action Code Validator"
echo "==============================="

if [ $# -eq 0 ]; then
    echo "Usage: $0 <action-file.txt>"
    echo "Example: $0 actions/my-action.txt"
    exit 1
fi

ACTION_FILE="$1"

if [ ! -f "$ACTION_FILE" ]; then
    echo "Error: File '$ACTION_FILE' not found!"
    exit 1
fi

echo "Validating: $ACTION_FILE"
echo ""

# Initialize counters
WARNINGS=0
ERRORS=0

# Function to report issues
report_warning() {
    echo "⚠️  Warning: $1"
    ((WARNINGS++))
}

report_error() {
    echo "❌ Error: $1"  
    ((ERRORS++))
}

report_success() {
    echo "✅ $1"
}

# Check for common syntax issues
echo "Checking syntax..."

# Check for unmatched brackets
OPEN_BRACES=$(grep -o '{' "$ACTION_FILE" | wc -l)
CLOSE_BRACES=$(grep -o '}' "$ACTION_FILE" | wc -l)

if [ "$OPEN_BRACES" -ne "$CLOSE_BRACES" ]; then
    report_error "Unmatched braces (${OPEN_BRACES} open, ${CLOSE_BRACES} close)"
else
    report_success "Braces are balanced"
fi

# Check for unmatched parentheses
OPEN_PARENS=$(grep -o '(' "$ACTION_FILE" | wc -l)
CLOSE_PARENS=$(grep -o ')' "$ACTION_FILE" | wc -l)

if [ "$OPEN_PARENS" -ne "$CLOSE_PARENS" ]; then
    report_error "Unmatched parentheses (${OPEN_PARENS} open, ${CLOSE_PARENS} close)"
else
    report_success "Parentheses are balanced"
fi

# Check for missing semicolons (more sophisticated check)
echo ""
echo "Checking statement termination..."
while IFS= read -r line; do
    # Skip empty lines and comments
    if [[ -z "$line" || "$line" =~ ^[[:space:]]*// ]]; then
        continue
    fi
    
    # Skip lines that are part of control structures
    if [[ "$line" =~ ^[[:space:]]*(if|else|while|for|\{|\}) ]]; then
        continue
    fi
    
    # Check if line ends with semicolon or brace
    if [[ ! "$line" =~ [\;\}][[:space:]]*$ ]]; then
        report_warning "Line may be missing semicolon: $line"
    fi
done < "$ACTION_FILE"

# Check for deprecated syntax and modern features
echo ""
echo "Checking syntax patterns..."

# Check for old comparison syntax
if grep -q '[^=!<>]=\s*[^=]' "$ACTION_FILE"; then
    report_warning "Found '=' for comparison - use '==' instead"
fi

# Check for unquoted string literals in comparisons
if grep -q '\$[A-Za-z][A-Za-z0-9]*\s*==\s*[A-Za-z][A-Za-z0-9]*[^;]' "$ACTION_FILE"; then
    report_warning "Possible unquoted string literal - quote string values"
fi

# Check for modern v10 features
echo ""
echo "Modern Tinderbox v10 features detected:"

# Check for dictionary usage
if grep -q 'dictionary(' "$ACTION_FILE"; then
    echo "  ✓ Uses Dictionary type (v10 feature)"
fi

# Check for stream processing
if grep -q '\.capture\|\.skip\|\.expect' "$ACTION_FILE"; then
    echo "  ✓ Uses stream processing (v10 feature)"
fi

# Check for advanced list methods
if grep -q '\.each(\|\.collect(\|\.any(\|\.every(' "$ACTION_FILE"; then
    echo "  ✓ Uses advanced list iteration (v10 feature)"
fi

# Check for JSON/XML processing
if grep -q 'JSON\.\|XML\.' "$ACTION_FILE"; then
    echo "  ✓ Uses JSON/XML processing (v10 feature)"
fi

# Check for fetch/API calls
if grep -q 'fetch(' "$ACTION_FILE"; then
    echo "  ✓ Uses HTTP/API functionality (v10 feature)"
fi

# Check best practices
echo ""
echo "Checking best practices..."

# Check for attribute name usage
echo ""
echo "Attribute usage found:"
ATTRS=$(grep -o '\$[A-Za-z][A-Za-z0-9]*' "$ACTION_FILE" | sort | uniq)
if [ -n "$ATTRS" ]; then
    echo "$ATTRS" | while read attr; do
        count=$(grep -c "$attr" "$ACTION_FILE")
        echo "  $attr (used $count times)"
    done
else
    report_warning "No attributes found - is this a valid action?"
fi

# Check for common functions
echo ""
echo "Functions/methods used:"
FUNCTIONS=$(grep -o '\.[a-zA-Z][a-zA-Z0-9]*(' "$ACTION_FILE" | sort | uniq)
if [ -n "$FUNCTIONS" ]; then
    echo "$FUNCTIONS" | sed 's/^/  /'
fi

# Check for control structures
echo ""
echo "Control structures:"
if grep -q 'if\s*(' "$ACTION_FILE"; then
    echo "  ✓ Uses conditional logic"
fi
if grep -q '\.each\s*(' "$ACTION_FILE"; then
    echo "  ✓ Uses iteration" 
fi
if grep -q 'var\s*(' "$ACTION_FILE"; then
    echo "  ✓ Uses local variables"
fi

# Check file size and complexity
echo ""
echo "File statistics:"
LINE_COUNT=$(wc -l < "$ACTION_FILE")
CHAR_COUNT=$(wc -c < "$ACTION_FILE")
echo "  Lines: $LINE_COUNT"
echo "  Characters: $CHAR_COUNT"

if [ "$LINE_COUNT" -gt 100 ]; then
    report_warning "Action is quite long ($LINE_COUNT lines) - consider breaking into smaller actions"
fi

# Final summary
echo ""
echo "Validation Summary:"
echo "=================="
if [ "$ERRORS" -eq 0 ] && [ "$WARNINGS" -eq 0 ]; then
    echo "✅ No issues found! Action appears to be well-formed."
else
    echo "Found $ERRORS errors and $WARNINGS warnings"
    if [ "$ERRORS" -gt 0 ]; then
        echo "❌ Fix errors before using this action"
    else
        echo "⚠️  Review warnings but action should work"
    fi
fi

echo ""
echo "Next steps:"
echo "1. Test action with sample data in Tinderbox"
echo "2. Check that all referenced attributes exist"  
echo "3. Verify the action produces expected results"
echo "4. Consider performance with large datasets"

exit $ERRORS