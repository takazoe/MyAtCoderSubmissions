if add_cnt == 0:
    # 何も追加していなければGitにアクセスしない
    print("No added submissions, end process")
else:
    # GitHubにプッシュ
    import git
    import datetime

    dt_now = datetime.datetime.now()
    repo_url = "https://github.com/tishii2479/atcoder.git"
    repo = git.Repo()
    repo.git.add("submissions/*")
    repo.git.commit("submissions/*", message="add submission: " + dt_now.strftime('%Y/%m/%d %H:%M:%S'))
    repo.git.push("origin", "main")

    print(f"Finished process, added {add_cnt} files")