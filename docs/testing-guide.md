# Action Testing Guide

## Testing Your Tinderbox Actions

Before deploying your action code to Tinderbox, it's important to validate the logic and syntax.

## Testing Checklist

- [ ] Syntax is correct (no missing semicolons, brackets)
- [ ] Variable names are spelled correctly
- [ ] Logic flow works as expected
- [ ] Edge cases are handled
- [ ] Performance is acceptable

## Common Testing Scenarios

1. **Empty/Null Values**: Test with empty attributes
2. **Special Characters**: Test with quotes, semicolons in text
3. **Large Text**: Test with lengthy note content
4. **Multiple Tags**: Test tag manipulation with existing tags
5. **Date Handling**: Test date comparisons and formatting

## Debugging Tips

- Use simple test cases first
- Add temporary output to verify variable values
- Test one condition at a time
- Check for case sensitivity issues
- Verify attribute names match exactly

## Example Test Data

Create test notes with:
- Priority: High, Medium, Low, (empty)
- Text containing keywords: meeting, project, todo
- Various tag combinations
- Different date ranges