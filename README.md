# Discord Screenshot Uploader
Large Image Uploading to S3 directly from the clipboard for easy sharing

Prefer to just resize your image? Don't care about sharing with full quality? Check out my other macro solution [Discord Screenshot Resizer](https://github.com/danetuso/discord-screenshot-resizer).

I've always been annoyed at the file size limit when trying to send a quick screenshot to a friend while playing games or attaching large images to work emails, so I created these tools.

## Example Usage (AutoHotKey Macro)
![Alt Text](https://github.com/danetuso/discord-screenshot-uploader/blob/main/macroexample.gif)
(Note that when you paste the direct link into discord or similar, the image preview will show automatically. There is no need to have the recipient download or open anything)

&nbsp;

## Windows Setup
---
## Bind the batch script to a macro key
I typically use AutoHotKey, but in this case I bound mine to my G6 key using Logitech G Hub software. The batch file must be in the same directory as the python script.
```
# Example AutoHotKey Macro Bind
# Ctrl + LShift + 6
^+6::
Run, C:\Path\To\launch_clipboardutil.bat
```

## Fill AWS credentials in the python script
I created an IAM user with policies to only allow this user to upload/putObjects, but all unauthenticated users can retrieve files from the specified bucket.

## Install Requirements
    pip3 install pillow boto3 pyperclip --target /path/to/directory/with/script/
(or use the included pip3 install -r requirements.txt)

&nbsp;

&nbsp;

## Windows Usage
---
## Save a screenshot to your clipboard
I typically use `Alt+PrintScrn` or `Win+Shift+S` but feel free to use your own method

## Hit your macro
Your image will be uploaded to the bucket automatically

## Paste
The clipboard is automatically overwritten to contain the url of the uploaded object. Paste directly into Discord, Slack, Gmail, etc.
