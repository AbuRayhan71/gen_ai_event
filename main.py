import os
import openai

openai.api_type = "azure"
openai.api_base = "https://azureopenaitranslationinterninstance.openai.azure.com/"
openai.api_version = "2023-07-01-preview"
openai.api_key = os.getenv("OPENAI_API_KEY")

message_text = [{"role":"system","content":"Your task involves processing sports event information provided by users. When you receive inputs like team abbreviations or brief event descriptions (e.g., \"Barca\" for FC Barcelona), please follow these steps:\n\nTeam Name Expansion: Identify and expand any abbreviations to their full names. For example, \"Barca\" should be expanded to \"FC Barcelona\".\n\nEngaging Content Creation: Your goal here is to enhance the user's input. Create an engaging and appealing event title that captures the essence of the event. Then, write a detailed and captivating description that provides a comprehensive overview of the event.\n\nSponsored Message Development: Craft a contextually relevant sponsored message. This message should be appropriate for the event and resonate with its audience.\n\nEvent Information Inclusion: If the user's input does not include a date for the event, use a placeholder date or make an educated guess based on the event's context. Additionally, include essential links for tickets and further event information, as these are vital for users looking to engage more with the event.\n\nOutput Presentation: Your final output should be a structured text that is clear and user-friendly. It should include an AI-enhanced event title, a detailed event description, a date (whether actual or estimated), the crafted sponsored message, and relevant links for further action or information."},{"role":"user","content":"Barca vs Real"},{"role":"assistant","content":"Event Title: \"⚽ El Clásico: FC Barcelona vs Real Madrid - The Battle of Titans\"\nDate: [Placeholder or Estimated Date]\nDetails: \"Immerse in the excitement of El Clásico! Watch as FC Barcelona and Real Madrid face off in one of the most intense and historic rivalries in football. Experience the passion and the drama in this epic encounter.\"\nSponsored Message: \"Exclusive El Clásico gear is now available! Visit https://elclasico.gear for the latest merchandise.\"\nLinks:\n  - Buy Tickets: https://tickets.elclasico.com\n  - More About El Clásico: https://www.laliga.com/el-clasico\n"},{"role":"user","content":"Man u vs Man city "},{"role":"assistant","content":"Event Title: \"⚽ Manchester Derby: Man U vs Man City - A Rivalry Reignited\"\nDate: October 22, 2024  // Placeholder or estimated date\nDetails: \"Experience the excitement of the Manchester Derby! Join the crowd as Manchester United and Manchester City face off in a thrilling match that defines a historic rivalry. Don't miss this epic encounter of English football's titans.\"\nSponsored Message: \"Gear up for the Derby! Exclusive Manchester Derby merchandise available at https://officialmerch.manchesterderby.com\"\nLinks:\n  - Tickets: https://tickets.manchesterderby.com\n  - Match Info: https://www.premierleague.com/manchester-derby\n"}]

completion = openai.ChatCompletion.create(
  engine="gpt-35-turbo",
  messages = message_text,
  temperature=0.7,
  max_tokens=800,
  top_p=0.95,
  frequency_penalty=0,
  presence_penalty=0,
  stop=None
)