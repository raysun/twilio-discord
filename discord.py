import sys
import os
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))

from discordWebhooks import Webhook, Attachment, Field

url = "https://discordapp.com/api/webhooks/272907589010980865/c8rT5C_NY55zh6zL9ja0VPCIMGOFhl5AKvrD8H611en17vjvY5TI2sgDEQeuSVn_o3Yo"
wh = Webhook(url, "Coucou tout le monde", "Pseudo")

at = Attachment(author_name = "Derpolino", color = "#ff0000", title = "Discord webhooks")

field = Field("Version", "1.0", True)
at.addField(field)
field = Field("Last update", "27/10/2016", True)
at.addField(field)
field = Field("Changelog", "Initiale release !", False)
at.addField(field)

wh.addAttachment(at)

at = Attachment(author_name = "Github", color = "#0000ff", title = "Hello world")
wh.addAttachment(at)

wh.post()
