# Reflection on Data Cleaning Project and Copilot Use

## What Copilot Generated

I used GitHub Copilot to help generate the structure and implementation of four main functions: `load_data()`, `clean_column_names()`, `handle_missing_values()`, and `remove_invalid_rows()`. I prompted Copilot by writing function signatures with type hints and docstrings that described what each function should do. For example, I wrote a comment like "Load sales data from CSV file" and Copilot suggested the pandas read_csv implementation. I also used Copilot to help organize the data validation logic, where it suggested using `dropna()`, numeric type conversion with `pd.to_numeric()`, and filtering for positive values.

## What I Modified

I made several important changes to Copilot's suggestions. First, I simplified the verbose docstrings that Copilot initially generated—it created long, multi-line descriptions with Args/Returns sections, but I condensed these to single-line summaries for clarity. Second, I modified the numeric conversion logic: Copilot initially suggested a simpler approach that didn't handle edge cases like strings with spaces or empty cells. I updated it to include `.astype(str).str.strip()` before conversion and use `errors="coerce"` to safely handle invalid values. Third, I reorganized the comment structure to be more concise, focusing on "what" and "why" rather than verbose explanations. Finally, I customized variable names and made the removal tracking logic clearer by tracking row counts at each step instead of Copilot's original approach.

## What I Learned

Working with Copilot taught me several important lessons about data cleaning and AI-assisted development. One key strength of Copilot is that it quickly suggests boilerplate code and common patterns—like using pandas for CSV operations—without me having to look them up. However, a major limitation is that it doesn't understand your specific file structure or data format. For example, when I first ran the script, Copilot had suggested generic file paths and didn't realize my columns had leading/trailing spaces. I had to manually debug this and add the `.str.strip()` step to the column name cleaning.

I also learned that data cleaning requires careful attention to edge cases. The raw dataset had issues like negative quantities (data entry errors), missing prices and quantities (represented as empty cells), and quoted text values. Copilot's initial suggestions handled some of these, but I had to enhance the logic to properly coerce non-numeric values to NaN and drop them consistently. Finally, I learned that clear comments are essential when working with AI—when I wrote specific comments like "Convert price to numeric type, coercing invalid entries to NaN," Copilot's suggestions were much more accurate than when I left it vague.

Overall, Copilot was most effective as a starting point for structure and common patterns, but required careful review, testing, and modification to handle the specific requirements of this dataset and project.
