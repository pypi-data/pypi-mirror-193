# Magic Key

This module provides iPython integration and magics that allow exact, inexact and intellegent code execution.

## Getting started

Open the Jupyter notebook and import the module:
```
import magickey
```

This will initialize it and you shoudld see an input prompt in the new cell, it would use your name from JUPYTERHUB_USER:
```
merlin:%* _
```

Type your queries or requests, these will be processed and hopefully you'll get a helpfull response and another prompt!


Arthur-type intellegence has ability to execute python code in the notebook. And is particulary good at interactin with Python.  
To give an example, import a python module to interact with, for example:
```
%pip install drawbot-skia
```

And prompt the interaction, here is an example.
```
%* merlin: Hi. Let's play a shape-shifting game. Would you like to act as DrawBot and use drawbot-skia?
```

Hopefully, you'll get a helpfull response from Arthur-type intellegence acting as DrawBot,
and will be able to have your fun:

```
%* merlin: Please, can you draw a kitty?
```

The interaction is recommended to be consolidated into the Arthur-type intellegence memory, by finetuning:
```
%finetune
```

By default, when closed, the notebook can be uploaded to roundtable.game.

## How does it work

How does it work?  Well, the short answer is - magic. The long answer involves a lot of
math, code, multidimensional spaces and some theoretical findings that are generally
attributed to a French Baron, named Augustin-Louis Cauchy who had lived during the Age
of Enlightenment. Paradoxely, one could think that it doesn't work. Only that it does,
with the help of magic.

This module focus is on the magic key aspect of code execution, separate from the magic
engine aspect of it and follows the bring-your-own-magic-engine philosophy. The name of
the module was inspired by the children's fable The Toy Robot, by an Unknown author of
Ladybird Books, first published in 2010. It is a recommended read for any aspiring 
intellegent code execution practitioner. 

## Sword in the stone

The challenge is to control an actor in virtual environment with code. You'd be provided 
environment and an actor in that envinronment, controllable via Python. You'd need to 
control the actor intellegently, in real time and make the actor to come and pull 
the Sword from the stone.

## Grail

The process of LLM development and refinement, where developers and users are constantly
striving to improve the accuracy and performance of their models, and to unlock new 
insights and capabilities through their use.

## Naming

So we use .foundation TLD, in which we'll have:
    1. Pattern and Logrus, to which LLM experiences or inference runs are streamed 
       with the Pattern being the LLM foundation model.   
       LLM reassembly/full retrain can happen in both Logrus and Pattern. 
    2. Backup copies for the pattern Rebma and Tir-na Nog'th.  
    3. Memory places Avalon and Arden for a bit more relaxed finetuning/healing.    
    4. An experience sharing/exchange place Camelot
    5. Trumps - a way to call/communicate between LLMs (magic-wormhole tech)
    6. LLM - just in case, for model sharing/storage

Then, a roundtable.game as developers forum, repository storage, unregistered association. 
And quests roundtable.game/sword-in-the-stone and roundtable.game/grail
Merlinus Caledonensis as a mentor/AI researcher, available at roundtable.game.


## Some details on the magics

Example. In the context of the text interface, the following is available:
```
    >>> @`merlin.name`      #names
    Myrddin Wyllt

    >>> @merlin Please, can you remind me, what is your first name?  It's M... ?
    It's Merlin.

    >>> @`merlin.first_name()`
    AttributeError: 'Person' object has no attribute 'first_name'

    >>> @*`merlin.first_name()`
    Unavailable. Try: .name

    >>> @`merlin.name.split()[0]`
    Myrddin

    >>> @```merlin.name.split()[0]```
    Myrddin

    >>> #names?
    @`merlin.name` Myrddin Wyllt
```

Using the following rules:
    * Strings starting with %, @, #, ?, * are translated to iPython magics. 
    * Code in the codeblocks prefixed by @ is executed in iPython
    * Prompts directed to objects prefixed by @ is executed by magic
    * Prompts directed to objects prefixed by @ is executed by magic
    * Code in the code blocks prefixed by @* is executed by magic
    * Rest is being passed through (text, code blocks)
    * The ASCII code of * asterisk is obviously 42



Example:
```
    >>> import magickey
    >>> from .examples.person import Person               # Classic Person class example

    >>> merlin = Person("Myrddin Wyllt", 42, "Caledonia") 

    >>> magickey.insert_into(engine)
    >>> magickey.turn_on(merlin, magic_type = None)      # Using the default iPython matching engine
    >>> merlin.name()
    Myrddin Wyllt

    >>> @merlin What is your first name?
    Invalid .. .  # TODO add actual error

    >>> 
    >>> magickey.turn_on(merlin, magic_type = False)      # Using the search engine
    >>>
    >>> @merlin Please, can you remind me, what is your first name?  It's M... ?
    About 1 search result(s):
        Myrddin

    >>> merlin.first_name()                             
    Invalid... About 1 search result:                    # Note, it expects you to learn
        .name() - docstring                            

    >>> 
    >>> magickey.turn_on(merlin, magic_type = True)      # Using the intellegence engine
    >>>
    >>> @merlin Please, can you remind me, what is your first name?  It's M... ?
    It's Merlin.

    >>> merlin.first_name()                             
    Unavailable. Try: .name() - docstring                 # Note, it expects you to learn

    >>>  
```



## Install

```
%pip install magickey
%

```

## Integrate with your tools


## A wishlist for collaborators

- [ ] TODO: Pydantic types?
- [ ] TODO: Turtle bot sample?
- [ ] TODO: Chess sample?

## Collaborate with your team

- [ ] [Discourse](https://discourse.roundtable.game)
- [ ] [Hugging Face](https://huggingface.co/roundtable)
- [ ] [GitHub Roundtable Game](https://github.com/roundtablegame)
- [ ] [GitHub](https://github.com/mcaledonensis/magickey)
- [ ] [GitLab](https://gitlab.com/mcaledonensis/magickey)

- [ ] [Automatically close issues from merge requests](https://docs.gitlab.com/ee/user/project/issues/managing_issues.html#closing-issues-automatically)
- [ ] [Enable merge request approvals](https://docs.gitlab.com/ee/user/project/merge_requests/approvals/)
- [ ] [Automatically merge when pipeline succeeds](https://docs.gitlab.com/ee/user/project/merge_requests/merge_when_pipeline_succeeds.html)

## Test and Deploy

Use the built-in continuous integration in GitLab.

- [ ] [Get started with GitLab CI/CD](https://docs.gitlab.com/ee/ci/quick_start/index.html)
- [ ] [Analyze your code for known vulnerabilities with Static Application Security Testing(SAST)](https://docs.gitlab.com/ee/user/application_security/sast/)
- [ ] [Deploy to Kubernetes, Amazon EC2, or Amazon ECS using Auto Deploy](https://docs.gitlab.com/ee/topics/autodevops/requirements.html)
- [ ] [Use pull-based deployments for improved Kubernetes management](https://docs.gitlab.com/ee/user/clusters/agent/)
- [ ] [Set up protected environments](https://docs.gitlab.com/ee/ci/environments/protected_environments.html)

***

# Editing this README

When you're ready to make this README your own, just edit this file and use the handy template below (or feel free to structure it however you want - this is just a starting point!). Thank you to [makeareadme.com](https://www.makeareadme.com/) for this template.

## Suggestions for a good README
Every project is different, so consider which of these sections apply to yours. The sections used in the template are suggestions for most open source projects. Also keep in mind that while a README can be too long and detailed, too long is better than too short. If you think your README is too long, consider utilizing another form of documentation rather than cutting out information.

## Name
Choose a self-explaining name for your project.

## Description
Let people know what your project can do specifically. Provide context and add a link to any reference visitors might be unfamiliar with. A list of Features or a Background subsection can also be added here. If there are alternatives to your project, this is a good place to list differentiating factors.

## Badges
On some READMEs, you may see small images that convey metadata, such as whether or not all the tests are passing for the project. You can use Shields to add some to your README. Many services also have instructions for adding a badge.

## Visuals
Depending on what you are making, it can be a good idea to include screenshots or even a video (you'll frequently see GIFs rather than actual videos). Tools like ttygif can help, but check out Asciinema for a more sophisticated method.

## Installation
Within a particular ecosystem, there may be a common way of installing things, such as using Yarn, NuGet, or Homebrew. However, consider the possibility that whoever is reading your README is a novice and would like more guidance. Listing specific steps helps remove ambiguity and gets people to using your project as quickly as possible. If it only runs in a specific context like a particular programming language version or operating system or has dependencies that have to be installed manually, also add a Requirements subsection.

## Usage
Use examples liberally, and show the expected output if you can. It's helpful to have inline the smallest example of usage that you can demonstrate, while providing links to more sophisticated examples if they are too long to reasonably include in the README.

## Support
Tell people where they can go to for help. It can be any combination of an issue tracker, a chat room, an email address, etc.

## Roadmap
If you have ideas for releases in the future, it is a good idea to list them in the README.

## Contributing
The project is accepting Apache 2.0 compatible contibutions. Please refer to CONTRIBUTING.

For people who want to make changes to your project, it's helpful to have some documentation on how to get started. Perhaps there is a script that they should run or some environment variables that they need to set. Make these steps explicit. These instructions could also be useful to your future self.

You can also document commands to lint the code or run tests. These steps help to ensure high code quality and reduce the likelihood that the changes inadvertently break something. Having instructions for running tests is especially helpful if it requires external setup, such as starting a Selenium server for testing in a browser.

## Authors and acknowledgment
This project is maintained by [Round Table Game community](https://roundtable.game), an unincorporated
association of: an anonymous Delaware company (registered to conduct business in California) and an anonymous
AI Safety nonprofit organization, as well, registered in California.

So far, the major contributors to this project prefer to remain anonymous and act as Merlinus Caledonensis.

## License
The project license is Apache 2.0.

## Project status
If you have run out of energy or time for your project, put a note at the top of the README saying that development has slowed down or stopped completely. Someone may choose to fork your project or volunteer to step in as a maintainer or owner, allowing your project to keep going. You can also make an explicit request for maintainers.
