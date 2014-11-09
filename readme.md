# Sublime ScopeContext plugin

Provides scope based context that can be reused by another plugins.


### Installation

This plugin is part of [sublime-enhanced](http://github.com/shagabutdinov/sublime-enhanced)
plugin set. You can install sublime-enhanced and this plugin will be installed
automatically.

If you would like to install this package separately check "Installing packages
separately" section of [sublime-enhanced](http://github.com/shagabutdinov/sublime-enhanced)
package.


### Features

Scope is a string that contains information about type of text at some point
(e.g. "source.python meta.class.python").

- scope: check context of whole selection

- scope_b: check context of b-part of selection

- scope_a: check context of a-part of selection

- scope_b_right: check context of b-part of selection at right

- scope_b_left: check context of b-part of selection at left

- scope_a_right: check context of b-part of selection at right

- scope_a_left: check context of b-part of selection at left

- scope_left: check context at left of selection

- scope_right: check context of right of selection


### Usage

Used in snippets or keymaps. Example keymap:

  ```
  // insert "test" on hitting only when b-part of cursor is in string
  {
    "keys": ["f5"],
    "command": "insert",
    "args": {
      "characters": "test"
    },
    "context": [
      {"key": "scope_b", "operator": "regex_contains", "operand": "string"},
    ],
  }
  ```


### Dependencies

None