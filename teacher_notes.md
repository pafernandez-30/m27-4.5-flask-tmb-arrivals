# Teacher Notes — TMB Arrivals

## Slot in sequence

After Week 4 (Birthdays SQL). Students have seen: routes, GET/POST, Jinja loops, db.execute queries.
This exercise introduces external API calls before Week 5 (ORM) and the Week 6 capstone.

## New concepts introduced

**`requests` library** — Python's standard HTTP client. `requests.get(url, params={...})` sends a GET request with query parameters appended automatically. Return value has a `.json()` method that parses the response body.

**External API as a data source** — the Flask route calls TMB's server, parses the response, and passes data to the template. The flow is: browser → Flask route → TMB API → parse JSON → template. This is the same client-server model as the Birthdays app, extended one level: Flask is now both a server (to the browser) and a client (to TMB).

**Nested data structure** — `stop_boards` is a list of dicts, each containing a list. This is the same pattern as `birthdays` but one level deeper. The template uses a nested Jinja loop to handle it.

**Credentials as config** — `TMB_APP_ID` and `TMB_APP_KEY` are module-level constants. Students replace the placeholder strings manually. Reinforce: credentials don't go on GitHub. In production these would be environment variables, but module-level constants are fine for a class exercise.

## Key Jinja pattern — nested loop

```html
{% for board in stop_boards %}        ← outer: one block per stop
    {% for bus in board.arrivals %}   ← inner: one row per bus
    {% endfor %}
{% endfor %}
```

This is the same structure as `{% for birthday in birthdays %}` from Week 4, but `board.arrivals` is itself a list. Draw the parallel explicitly when demoing.

## JSON response structure

```json
{
  "data": {
    "ibus": [
      {"line": "H6", "text": "3 min", "destination": "Feixa Llarga"},
      {"line": "75", "text": "8 min", "destination": "Pl. Espanya"}
    ]
  }
}
```

`response.json()["data"]["ibus"]` drills to the array. Common student mistake: accessing the wrong key level (e.g. `response.json()["ibus"]` — missing the `"data"` wrapper).

## TMB API credentials

Class key distributed in person. Nuke after the exercise. The `TMB_APP_ID` and `TMB_APP_KEY` placeholders in the repo are intentionally inert — students who forget to update them will get a 401 error, which is a useful debugging moment.

## Common mistakes

- **Wrong JSON path** — `response.json()["ibus"]` instead of `response.json()["data"]["ibus"]`. Have students print the raw response to inspect the structure.
- **Stop not in TMB pool** — stops served by partner operators (some Esplugues/L'Hospitalet stops) return an empty or error response. If a student's stop returns nothing, have them check the TMB website first.
- **Forgetting to add the stop name** — they add an `id` but no `name` key, causing a KeyError in the template. The comment scaffold in STOPS shows both keys.

## Differentiation

- **Done early:** Add a `{% if board.arrivals %}` check in the template so stops with no current buses show a friendly message instead of an empty table.
- **Extension:** Add a refresh link or a `<meta http-equiv="refresh">` tag so the page auto-reloads every 30 seconds.
- **Discussion:** Why does the page feel slow when you have three stops? (Three sequential API calls.) What would make it faster? (Parallel requests — but that's async, which is beyond scope.)
