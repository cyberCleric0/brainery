## General Data Tables

|Table Name|Description|
|---|---|
|media|Base table for learning resources|
|media_types|holds various media types such as book, ebook, video|
|creator|names of authors, presenters, etc.|
|roles|various roles for the content creators|
|publisher|content publisher companies|
|content_type|various content types (DELETED)|
|location|options for where the item is stored (Web, local storage, etc)|
|codec|options for media codecs|
|resolution|options for video resolutions|
|video|stores information relevant to videos|
|website|stores information about websites that host content|
|book|stores information relevant to books|
|category|categories and subcategories using parent_id|
|format|book formats (pdf, ePub, etc)|
|format_extensions **deleted**|Extensions of various formats - I think I can/should delete this.|
|filename|stores the filenames of resources. More than one can be assigned per resource|

## Cross-Reference Tables

|Table|X-Ref|X-Ref|
|---|---|---|
|mediaXcreator|media(id)|creator(id)|
|mediaXpublisher|media(id)|creator(id)|
|mediaXcontent_type **deleted**|media(id)|content_type(id)| 
|videoXresolution|video(id)|resolution(id)|
|mediaXwebsite|media(id)|website(id)|
|mediaXlocation|media(id)|location(id)|