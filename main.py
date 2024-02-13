import os
import openai

openai.api_type = "azure"
openai.api_base = "https://aitranslationus2.openai.azure.com/"
openai.api_version = "2023-07-01-preview"
openai.api_key = os.getenv("OPENAI_API_KEY")

message_text = [{"role":"system","content":"Given a CSV line 'Sheffield United v Tottenham Hotspur, 2024-05-19, Bramall Lane, Sheffield, Live coverage on: Check your local guides | #SHUTOT, Play the biggest Fantasy Football game in the world. Register here: https://ql.e-c.al/PLfantasy, https://www.premierleague.com/broadcast-schedules', extract and enhance key components - Name, Date, Location, Details, Sponsored Message, and Links. Add an emoji to the Name, format the Date, ensure proper capitalization for Location, and clearly format Details, Sponsored Message, and Links. Finally, transform this into a structured JSON object with fields for event_id, name, genre, sub-genre, and the enhanced elements. If the event_id matches an existing one in the database, update the record with this new data."},{"role":"user","content":"Given CSV line: \"Sheffield United v Tottenham Hotspur, 2024-05-19, Bramall Lane, Sheffield, Live coverage on: Check your local guides | #SHUTOT, Play the biggest Fantasy Football game in the world. Register here: https://ql.e-c.al/PLfantasy, https://www.premierleague.com/broadcast-schedules\""},{"role":"assistant","content":"Transform the formatted data into a structured JSON object:\n\n{\n  \"event_id\": \"ObjectId(648ae781354b70d5043658de)\",\n  \"name\": \":football:️ Sheffield United v Tottenham Hotspur\",\n  \"genre\": \"\",\n  \"sub-genre\": \"\",\n  \"details\": \"Live coverage on: Check your local guides | #SHUTOT\",\n  \"location\": \"Bramall Lane, Sheffield\",\n  \"date\": \"2024-05-19\",\n  \"sponsored_message\": \"Play the biggest Fantasy Football game in the world. Register here: https://ql.e-c.al/PLfantasy\",\n  \"links\": {\n    \"TV Schedule\": \"https://www.premierleague.com/broadcast-schedules\"\n  }\n}\n\nNote: Each 'event_id' should be a unique identifier.\n"},{"role":"user","content":"{  \n  \"event_id\": \"574cf4b7cfc6287e010044f1\",  \n  "},{"role":"assistant","content":"{  \n  \"event_id\": \"574cf4b7cfc6287e010044f1\",  \n  \"name\": \"⚽️ Crystal Palace v Aston Villa\",  \n  \"genre\": \"Sports\",  \n  \"sub-genre\": \"Football\",  \n  \"details\": \"Live coverage on: Check your local guides | #CRYVIL. Follow the match live on the Official Crystal Palace app.\",  \n  \"location\": \"Selhurst Park, London\",  \n  \"date\": \"2024-05-19\",  \n  \"sponsored_message\": \"Play the biggest Fantasy Football game in the world. Register here.\",  \n  \"links\": {  \n    \"Official App\": \"https://ql.e-c.al/cpfcapp\",  \n    \"TV Schedule\": \"https://www.premierleague.com/broadcast-schedules\",  \n    \"Match Centre\": \"https://www.premierleague.com/fixtures\",  \n    \"Club Shop\": \"https://shop.cpfc.co.uk/\",  \n    \"Twitter\": \"https://twitter.com/CPFC\"  \n  }  \n}  "},{"role":"user","content":"ObjectId(648ae052354b70d7283819c9)\tObjectId(593a3dba20058a56418b4568)\t10365\tâš½ï¸ Brighton & Hove Albion v Manchester United\t\"Live coverage on: Check your local guides | #BHAMUN\n\nFollow the match live on the Official Brighton & Hove Albion app: https://ql.e-c.al/brightonapp\"\tAmerican Express Stadium, Falmer\t19/05/2024\tPlay the biggest Fantasy Football game in the world. Register here: https://ql.e-c.al/PLfantasy\tTV Schedule\thttps://www.premierleague.com/broadcast-schedules\thttps://www.premierleague.com/broadcast-schedules\tMatch Centre\thttps://www.premierleague.com/fixtures\thttps://www.premierleague.com/fixtures\tBrighton & Hove Albion Shop\thttps://shop.brightonandhovealbion.com/\thttps://shop.brightonandhovealbion.com/\tBrighton & Hove Albion Twitter\thttps://twitter.com/OfficialBHAFC\thttps://twitter.com/OfficialBHAFC"},{"role":"assistant","content":"Based on the new input provided, the structured JSON object for the Brighton & Hove Albion v Manchester United match would look like this:\n\n```json\n{\n  \"event_id\": \"648ae052354b70d7283819c9\",\n  \"name\": \"⚽️ Brighton & Hove Albion v Manchester United\",\n  \"genre\": \"Sports\",\n  \"sub-genre\": \"Football\",\n  \"details\": \"Live coverage on: Check your local guides | #BHAMUN. Follow the match live on the Official Brighton & Hove Albion app.\",\n  \"location\": \"American Express Stadium, Falmer\",\n  \"date\": \"2024-05-19\",\n  \"sponsored_message\": \"Play the biggest Fantasy Football game in the world. Register here: https://ql.e-c.al/PLfantasy\",\n  \"links\": {\n    \"Official App\": \"https://ql.e-c.al/brightonapp\",\n    \"TV Schedule\": \"https://www.premierleague.com/broadcast-schedules\",\n    \"Match Centre\": \"https://www.premierleague.com/fixtures\",\n    \"Club Shop\": \"https://shop.brightonandhovealbion.com/\",\n    \"Twitter\": \"https://twitter.com/OfficialBHAFC\"\n  }\n}\n```\n\nPlease note that the date is formatted to \"YYYY-MM-DD\" for standardization, the name of the event is now prefixed with a football emoji, the location is properly capitalized, and the links are appropriately categorized under a \"links\" object. The event_id provided, \"648ae052354b70d7283819c9\", should be used to identify the record in the database for updating. If the event_id does not exist, a new record with this information should be created."},{"role":"user","content":"\"event_id\": \"648ae052354b70d7283819c9\""},{"role":"user","content":"\"event_id\": \"648ae052354b70d7283819c9\""},{"role":"assistant","content":"Based on the provided event_id \"648ae052354b70d7283819c9\", here is the structured JSON object with the complete information from the given CSV data for the event:\n\n```json\n{\n  \"event_id\": \"648ae052354b70d7283819c9\",\n  \"name\": \"⚽️ Brighton & Hove Albion v Manchester United\",\n  \"genre\": \"Sports\",\n  \"sub-genre\": \"Football\",\n  \"details\": \"Live coverage on: Check your local guides | #BHAMUN. Follow the match live on the Official Brighton & Hove Albion app.\",\n  \"location\": \"American Express Stadium, Falmer\",\n  \"date\": \"Sunday, May 19, 2024\",\n  \"sponsored_message\": \"Play the biggest Fantasy Football game in the world. Register here: https://ql.e-c.al/PLfantasy\",\n  \"links\": {\n    \"Official App\": \"https://ql.e-c.al/brightonapp\",\n    \"TV Schedule\": \"https://www.premierleague.com/broadcast-schedules\",\n    \"Match Centre\": \"https://www.premierleague.com/fixtures\",\n    \"Club Shop\": \"https://shop.brightonandhovealbion.com/\",\n    \"Twitter\": \"https://twitter.com/OfficialBHAFC\"\n  }\n}\n```\n\nThis JSON object should be used to update the database record with the corresponding event_id. If a record with this event_id does not exist, a new one should be created with the provided information. The date has been formatted to a more readable form (e.g., \"Sunday, May 19, 2024\"), and the links have been organized under the \"links\" object for clarity."},{"role":"user","content":"Sheffield United v Tottenham Hotspur"},{"role":"assistant","content":"Based on the event name \"Sheffield United v Tottenham Hotspur\" and the previously provided event_id \"648ae052354b70d7283819c9\", here is the structured JSON object that reflects the updated information for this specific football match:\n\n```json\n{\n  \"event_id\": \"648ae052354b70d7283819c9\",\n  \"name\": \"⚽️ Sheffield United v Tottenham Hotspur\",\n  \"genre\": \"Sports\",\n  \"sub-genre\": \"Football\",\n  \"details\": \"Live coverage on: Check your local guides | #SHUTOT\",\n  \"location\": \"Bramall Lane, Sheffield\",\n  \"date\": \"Sunday, May 19, 2024\",\n  \"sponsored_message\": \"Play the biggest Fantasy Football game in the world. Register here: https://ql.e-c.al/PLfantasy\",\n  \"links\": {\n    \"Fantasy Football\": \"https://ql.e-c.al/PLfantasy\",\n    \"Broadcast Schedules\": \"https://www.premierleague.com/broadcast-schedules\"\n  }\n}\n```\n\nThis JSON object is based on the initial CSV line you provided and the given event_id. It should be used to update the database record with the corresponding event_id. The date has been formatted for readability, and the emoji has been added to the event name to signify that it is a football match. The details, sponsored message, and links are clearly formatted and presented. If the record with this event_id does not exist in the database, a new record should be created with this information."},{"role":"user","content":"Arsenal v Aston Villa"},{"role":"user","content":"Arsenal v Aston Villa"},{"role":"assistant","content":"It seems like you've provided the event name \"Arsenal v Aston Villa\" without additional context or data. If you're looking to create a structured JSON object for an event with this name, we'd need more information such as date, location, event details, sponsored messages, and relevant links.\n\nHere's an example of what a structured JSON object might look like for an \"Arsenal v Aston Villa\" match, with hypothetical data:\n\n```json\n{\n  \"event_id\": \"exampleEventId123456\",\n  \"name\": \"⚽️ Arsenal v Aston Villa\",\n  \"genre\": \"Sports\",\n  \"sub-genre\": \"Football\",\n  \"details\": \"Tune in for a thrilling match between Arsenal and Aston Villa. Don't miss any action!\",\n  \"location\": \"Emirates Stadium, London\",\n  \"date\": \"YYYY-MM-DD\", // Replace with the actual date in the format Year-Month-Day\n  \"sponsored_message\": \"Join the excitement and play the official Fantasy Premier League. Sign up now!\",\n  \"links\": {\n    \"Fantasy Premier League\": \"https://fantasy.premierleague.com/\",\n    \"Tickets\": \"https://www.arsenal.com/tickets\",\n    \"Broadcast Schedule\": \"https://www.premierleague.com/broadcast-schedules\"\n  }\n}\n```\n\nPlease replace the `event_id`, `date`, `details`, `sponsored_message`, and URLs with the correct information. The `event_id` should be unique for each event. If this JSON object is intended to update an existing record in a database, please ensure that the `event_id` matches the one in the database. If there's no matching `event_id`, a new record should be created with the provided information."}]

completion = openai.ChatCompletion.create(
 engine="gpt4",
 messages = message_text,
  temperature=0.7,
  max_tokens=800,
  top_p=0.95,
 frequency_penalty=0,
 presence_pen