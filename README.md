# News-Highlights
### May 20th 2019
#### By **[Purity Sowayi]** (https://github.com/apwao)
## Description
This is an application that allows the users to view news provided by various sources on a variety of topics.
## Setup/Installation Requirements
* Fork the repository into your account.
* Clone the repository to your local machine
* Activate a virtual environment using the command: source  virtual/bin/activate on your terminal
* Install all the requirements within the requirements file.
* Replace the api_key in the start.sh file with your own  generated from: https://news.org
* Run the command chmod a+x start.py on your terminal
* Run the command ./start.py
* Access the live site through a browser using the local host provided
## BDD
|Behavior                     |Input                 |Output
|-----------------------------|----------------------|--------------------------------------------
|User clicks on a news source | ABC news             | Displays news articles from ABC news profile
|User clicks on readmore...   | Readmore...          | Redirects user to the original source 
|User views homepage          | Navigates to homepage| Displays news from all sources
## Known Bugs
* No bugs
## Technologies Used
* CSS
* Git
* Flask
* Python3.6
* HTML
* Bootstrap
* JQuery

## Support and contact details
Incase of any issues, ideas, questions or concerns, contact contributor at pasowayi@gmail.com.
In order to contribute to the code: Fork a copy of the repository, push changes to a branch called contributions. Issue a pull request to the contributor.
### License
Copyright (c) 2019 **Purity Sowayi**
MIT License

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
