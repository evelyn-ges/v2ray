# your link goes here
link = "https://github.com/evelyn-ges/v2ray/blob/main/rg"

# note: this will break if a repo/organization or subfolder is named "blob" -- would be ideal to use a fancy regex
# to be more precise here
print(link.replace("github.com", "raw.githubusercontent.com").replace("/v2ray/", "/"))

# example output link:
# https://raw.githubusercontent.com/evelyn-ges/v2ray/blob/main/rg
