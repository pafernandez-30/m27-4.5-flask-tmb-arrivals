# TMB Bus Arrivals

A Flask app that shows live bus departure times using the TMB public transit API.

## Setup

1. Save the `.env` file provided in class into this folder. It contains the API credentials — do not share it or push it to GitHub (it is already listed in `.gitignore`).

2. Run the app:
   ```
   flask run --debug
   ```

3. Open the app in your browser. You should see live arrivals for Zona Universitaria (stop 556).

## Your task

Add two more stops from your own life — your neighbourhood, your usual metro connection, wherever.

**Finding your stop ID:**

Every bus stop has a 3–5 digit code printed on the shelter sign. You can also find it at:
```
https://www.tmb.cat/en/barcelona/autobusos/-/lineabus/parada/STOPID
```
Replace `STOPID` with the number from the sign.

**Adding a stop:**

In `app.py`, find the `STOPS` list and uncomment the TODO lines:

```python
STOPS = [
    {"id": 556, "name": "Zona Universitaria"},
    {"id": 1747, "name": "My stop"},   # ← add yours here
]
```

Once you add an entry to `STOPS`, it appears automatically on the page — no other changes needed.
