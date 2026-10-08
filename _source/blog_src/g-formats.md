![JSON vs YAML vs CSV: Which Data Format Uses the Fewest Tokens?](/json-vs-yaml-vs-csv-tokens-en.jpg)

When you send data to an AI model, whether product lists, survey results, database rows or API responses, the format you choose changes how many tokens it takes. We measured the same table in seven common formats on GPT's o200k tokenizer. The most popular choice, pretty-printed JSON with one object per row, uses almost three times as many tokens as the cheapest. The same data as columnar JSON costs about the same as CSV: the expensive part is repeating the keys, not JSON itself.

*Updated October 3, 2026: added columnar JSON and header-plus-rows JSON after a reader pointed out they were missing. Same table, same tokenizer.*

## The test

We took a small product table: 20 rows, 5 fields each (an ID, a product name, a price, an in-stock flag and a category). Then we wrote the exact same data in seven formats and counted tokens.

A row looks like this in CSV:

    1001,Wireless Mouse,9.99,false,electronics

## Results

![Results: Format, Tokens, vs CSV, Characters](/json-vs-yaml-vs-csv-tokens-results-en.jpg)

| Format | Tokens | vs CSV | Characters |
|---|---|---|---|
| TSV (tab-separated) | 296 | 0.99× | 891 |
| CSV | 300 | 1.00× | 891 |
| JSON, columnar, minified `{"id":[...],"name":[...]}` | 297 | 0.99× | 993 |
| JSON, header + row arrays | 320 | 1.07× | 1,044 |
| Markdown table | 373 | 1.24× | 1,165 |
| JSON, columnar, pretty-printed | 520 | 1.73× | 1,529 |
| JSON, one object per row, minified | 525 | 1.75× | 1,821 |
| YAML | 649 | 2.16× | 1,799 |
| JSON, one object per row, pretty-printed (2-space indent) | 884 | 2.95× | 2,542 |
| XML | 1,088 | 3.63× | 3,362 |

Measured with the o200k tokenizer used by GPT-4o and later. The older cl100k tokenizer gave almost identical results, within 2% for every format.

## Why the gap is so big

**Keys are repeated on every row.** JSON, YAML and XML write the field name again for every record: `"name":`, `"price":`, `"in_stock":` twenty times over. CSV, TSV and Markdown write each field name once, in the header. So does columnar JSON, which puts one array per field inside a single object, and that is why it lands right next to CSV.

**Punctuation costs tokens.** Every quote mark, brace, colon and comma in JSON is part of a token, and many become tokens of their own. XML is worst because every value is wrapped in an opening and a closing tag.

**Pretty-printing adds structure, not meaning.** Line breaks and indentation make JSON readable for people. The model does not need them, and in this test they added 359 tokens (68%) compared with the minified version.

YAML is interesting: it has fewer characters than minified JSON but more tokens, because it puts every field on its own line with its own key.

## What this costs at scale

![What this costs at scale: Format, Tokens per month, Cost per month](/json-vs-yaml-vs-csv-tokens-what-this-costs-at-scale-en.jpg)

Suppose an app sends a 20-row table like this with every request, 1,000 times a day. Over a month that is 30,000 requests. At an input price of $2 per million tokens (GPT-6 Sol, checked October 1, 2026):

| Format | Tokens per month | Cost per month |
|---|---|---|
| CSV | 9.0M | $18 |
| JSON, columnar | 8.9M | $18 |
| JSON, one object per row, minified | 15.8M | $32 |
| JSON, one object per row, pretty-printed | 26.5M | $53 |
| XML | 32.6M | $65 |

The difference is small for one request and real for a product. For larger tables, retrieval results or long API responses pasted into prompts, it grows in proportion.

## Which format should you use?

**For flat tables you send as input: CSV or TSV.** They are the cheapest, and current models read them well. Use TSV if your values contain commas, so you do not need quoting.

**If the input has to be JSON: columnar or header plus row arrays.** You keep valid JSON and pay roughly what CSV costs.

**For data the model must return: minified JSON with a schema.** Many APIs offer structured output modes that guarantee valid JSON matching a schema you provide. That reliability is usually worth more than the tokens you would save with CSV, and you can keep field names short.

**For nested data: minified JSON.** CSV cannot represent nesting cleanly, and flattening it by hand often costs more tokens than it saves.

**For tables a person will also read: Markdown.** Only 24% more than CSV and much easier to check by eye.

**Avoid pretty-printed JSON and XML in prompts** unless a tool requires them.

## Other ways to shrink structured data

![Other ways to shrink structured data: Send only the fields the task needs. If the model is writing product descriptions, it probably does not need i](/json-vs-yaml-vs-csv-tokens-other-ways-to-shrink-structured-data-en.jpg)

1. **Send only the fields the task needs.** If the model is writing product descriptions, it probably does not need internal IDs, timestamps or warehouse codes.
2. **Shorten long values.** Replace long IDs with row numbers and map them back in your code afterwards. A standard UUID is 18 tokens on its own.
3. **Round numbers.** `9.99` is cheaper than `9.990000001`, and most tasks do not need the extra digits.
4. **Drop empty fields.** `"notes": null` on every row is pure overhead.

## Caveats

These numbers come from one table on one tokenizer. Claude and Gemini use different tokenizers, so absolute counts will differ, but the ranking (tabular formats cheapest, repeated keys and tags most expensive) follows from how the formats are built and holds generally. If the format affects accuracy for your task, test both: a cheaper prompt that gives worse answers is not cheaper.

## Measure your own data

Paste a sample of your data into the [token counter](/) in two formats and compare. It runs the same o200k tokenizer in your browser, and nothing you paste is uploaded.
<!-- autoimg -->
