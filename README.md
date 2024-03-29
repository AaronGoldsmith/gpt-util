# gpt-util
Reusable GPT utility scripts 

### Git Hooks 


git hooks are automatically added to your project whenever you initialize or clone a repository. All hooks can be found in the `.git/hooks` folder. 

```bash 
$ ls path/to/your/repository/.git/hooks/
```

<pre>
applypatch-msg.sample     pre-applypatch.sample     pre-rebase.sample         update.sample
commit-msg.sample         pre-commit.sample         pre-receive.sample
fsmonitor-watchman.sample pre-merge-commit.sample   prepare-commit-msg.sample
post-update.sample        pre-push.sample           push-to-checkout.sample
</pre>

To use a hook, rename the file without the `.sample` suffix.

use `chmod +x <path to file>` to set the execute (x) permission on the perl file

For a more in depth overview on Git Hooks, I reccomend [Atlassian's Tutorial](https://www.atlassian.com/git/tutorials/git-hooks)

[Auto Commit Message](hooks/prepare-commit-msg): Instruct GPT3.5 to review the modified code and summarize the changes. 