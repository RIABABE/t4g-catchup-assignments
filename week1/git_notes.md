
A Git conflict occurs when two different branches have made changes to 
the same part of the same file, and Git cannot automatically decide 
which version to keep when merging.


Step 1
 See which file has the conflict
git status

Step 2 
Open that file and find the markers
nano filename.md

Step 3 
Pick the version you want to keep and delete everything else

Step 4 
Save the file, then tell Git you fixed it
git add filename.md

Step 5 
Complete the merge
git commit -m "Resolve merge conflict in filename.md"


After resolving, your file must look completely normal with zero conflict markers remaining. 
