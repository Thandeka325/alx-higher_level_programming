# __Project: 0x14-javascript-web_scraping__

This is an introduction too Java Script, how it can be used.

__Resources__

- [Working with JSON data](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Scripting/JSON)
- [The workflow of accessing the attributes of a simply-created JSON object by Jimmy Tran from Cohort 1 - San Francisco](https://medium.com/@vietkieutie/the-workflow-of-accessing-the-attributes-of-a-simply-created-json-object-82a5b33e2319)
- [request module](https://github.com/request/request)
- [Modern JS](https://github.com/mbeaudru/modern-js-cheatsheet)

__More Info__

Install Node 14
```
$ curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
$ sudo apt-get install -y nodejs
```

Install semi-standard
[Documentation](https://github.com/standard/semistandard)

```
$ sudo npm install semistandard --global
```

Install request module and use it
[Documentation](https://github.com/request/request)

```
$ sudo npm install request --global
$ export NODE_PATH=/usr/lib/node_modules
```
__Notes__: Request module has been deprecated since February 2020 - the team is considering alternative to replace this module - however, it’s a really simple and powerful module for practicing web-scraping in JavaScript (and still used a lot in the industry).
