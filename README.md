# sub-ocr
> ocr and optional image merge

Bulk merge images vertically. Highly accurate Chinese OCR using Baidu. Optional programs to install if you want to create subtitles: VideoSubFinder, SubtitleEdit

## Installation

```python
pip install baidu-aip
```

## Normal Accuracy (50,000 quota) VS High Accuracy (500 quota)

basicGeneral is normal accuracy. basicAccurate is high accuracy. Only use one of them.
```python
result = client.basicGeneral(image)
result = client.basicAccurate(image)
```

## Usage example

Use moveandmerge.py to bulk merge images vertically.
FYI, ImageMerge.exe can be used on its own. It works by looking inside "Old Images" then "Merged Images".

What is the difference between baiduhigh.py and baiduocr.py?
Use baiduhigh.py only if the images are saved in the timestamp filename format from VideoSubFinder. Results are saved in multiple text files. Then the srt is created based on the timestamp filenames.
Use baiduocr.py for everything else including merged images. Results are saved in a single text file.


## Obtain your API_KEY (requires phone #)
Instructions in Chinese https://ai.baidu.com/ai-doc/REFERENCE/Ck3dwjgn3
~~My instructions: Follow method 2 from here https://www.infinityfolder.com/how-to-create-a-baidu-account-from-outside-china/. Skip the adding email part.~~
Then click the blue button from here https://ai.baidu.com/tech/ocr/general. Then https://imgur.com/a/v6PIjUP.
Edit as of 2020, new Baidu account creation has been disabled for overseas users...

## Complete guide on how to extract subtitles with VideoSubFinder
Download VideoSubFinder. Go to \VideoSubFinder_4.30_x64\Release_x64\settings, open general.cfg in Notepad++. Change min_sum_color_diff = 800 (high number reduces amount of blank images), vedges_points_line_error = 0.15 (the default is 0.3 which works for most videos but sometimes it misses subtitles so I use 0.15) (low number will capture all subtitles with short gaps, but more duplicate images)
Make a box big enough for two lines of subtitles. Run search. https://i.imgur.com/TYOKmu5.jpg. After scanning, RGBImages folder is now full.

METHOD 1: the most automated without merging images. But it quickly consumes your 500 image quota which resets at midnight.
```python
python baiduhigh.py
```
Please use your own APP_ID, API_KEY, SECRET_KEY.

After all images have been ocr'd. The srt is automatically created.

Cleaning Up the Subtitles and Retiming
1. Find blank lines and delete them. 2. Open Subtitle Edit > Tools > Merge Lines With Same Text > any number between 0 and 888 milliseconds. To retime, synchronization > Adjust time > Selected lines and forward.
Btw mpv is a useful video player because by pressing ctrl right arrow, it will take you to the next subtitle. Aegisub is another good software.

Translating from Chinese to English
In my opinion, https://www.deepl.com/translator is the most accurate. Open Subtitle Edit > File > Export as txt. Copy and paste into Deepl. Copy and paste the English results in another txt file. Open Subtitle Edit, drag and drop the English txt file. File > Import time codes > select the srt. If the number of timestamps and lines don't match, then there are blank lines somewhere.

METHOD 2: requires additional effort and more software. A really long picture still counts as one images so it's unlikely to go over your quota.
1. Create empty sub in VideoSubFinder
2. Bulk crop images with IrfanView.
3. Merge with moveandmerge.py
4. OCR with baiduocr.py (all results saved in a single txt file) or QQ OCR https://ai.qq.com/product/ocr.shtml#common (remove numbers with regular expressions in Notepad++)
5. Type /N in between double lines. Make sure the # of lines match in Notepad++. Recommended image viewer is Honeyview because it displays the current image count. Combine txt and srt in Aegisub with ctrl shift v
6. Clean up in SubtitleEdit.

## FAQ
What to do if I reach the 500 quota?
Wait until midnight for your quota reset or create another Baidu Cloud account with a free phone number app such as TextNow.

What is Baidu's image height limit?
About ~2500 pixels

How to change the amount of pics to merge?
Inside moveandmerge.py, change picAmount

My video already has embedded DVB subtitles. How to access them?
Images in png format and srt that can be accessed with Subtitle Edit. https://i.imgur.com/z3yEoQ7.jpg

## References

API, SDK documentaion: Baidu-AIP on github or https://ai.baidu.com/ai-doc/OCR/Ek3h7xypm
