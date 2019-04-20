# Corgi Website Files for IS590DV at UIUC

These are files that have been used to build test Idyll websites in class for [our spring class both online and in person](https://uiuc-ischool-dataviz.github.io/spring2019online/).  

Data parsed from the [Cardiped database](http://www.cardiped.net/).

## Install Instructions

These are taken from [week 10 install instructions](https://uiuc-ischool-dataviz.github.io/spring2019online/week10/).

A video of this process (with errors & explaination) for Macs can be <a href="https://youtu.be/mWxXmWk_vDU">found right here</a>.

A video of this process (with errors & explaination) for Windows 10 can be <a href="https://youtu.be/nQ2FFGzREos">found right here</a> (and see notes at the end of this section).


1. Install Idyll:
```
npm install -g idyll
```
1. Create new post with idyll
```
idyll create
```
1. cd into post directory
1. Install dependencies to install vegalite
```
npm install --save acorn@^6.0.0 vega-lite@^2.0.0 react@^16.0.0 react-dom@^16.0.0 vega@^3.3.1
```
1. Install vegalite for Idyll
```
npm install --save idyll-vega-lite
```
1. Copy <a href="idyll_website/index.idyll" download>index.idyll</a> to your post directory
1. Update <a href="idyll_website/package.json" download>package.json</a> file to match the linked one
1. Build this website with
```
idyll
```

**Notes for Windows install:**

* You need to have Nodejs installed - <a href="https://nodejs.org/en/download/">download link here</a>. You will have to restart your computer.
* You need to have git installed - <a href="https://git-scm.com/">download link here</a>.  You will have to restart your computer.


