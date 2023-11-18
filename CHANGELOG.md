# CHANGELOG



## v0.6.0 (2023-11-18)

### Build

* build: update dockerfile for new dir structure ([`0f1e8c0`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/0f1e8c0f3bfbc1610c159ea6e0f0c40cc86bd1b1))

### Ci

* ci: fix integration tests with new path (#200)

Auto-created ([`b734f9e`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/b734f9ee8f103586cdf7718ae13a50bf9dc5eb12))

* ci: run docker publish independently of integration test ([`d1402c6`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/d1402c6a29d5ef2878ed8342ca237edb5d3b5ae5))

* ci: run type checks on application script as well ([`849c0f5`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/849c0f552ae9ae785bdb515d480dca811f0436ef))

* ci: setup multiplatform conditions (#192) ([`5120b18`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/5120b18685cce3af0930473d8981d5f87e0016c0))

* ci: add arm64 to deploy ([`a6fb2c5`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/a6fb2c58b1ef39ead800263a33b2e56210c8f9dc))

* ci: update docker build action ([`6724cd4`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/6724cd4c6475924d5780420d6446e5d869c82cda))

### Feature

* feat: move cli to separate file ([`f91216b`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/f91216b9cf9fdd04eb7227de4b7d497472dc4ccd))

### Fix

* fix: do not mount input dir on remote (#201)

Auto-created ([`83cedae`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/83cedaeb83c918248d52ad2f09233232761972b6))

* fix: add mounts points for devcontainer ([`c2497ee`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/c2497eeb7a0cc76763d45db4694b1a0c9d6d55ac))

### Refactor

* refactor: rename pipeline to not hit test ([`1b5cbf2`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/1b5cbf2ed84aa1459853cf143509f690ede4ea79))

### Unknown

* misc. ([`b81c54a`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/b81c54a8dfc946adc83547d66f1b6c858336814e))

* misc. ([`cb6d386`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/cb6d3866efa654ecd182f27161eaae090fe19f20))

* misc. ([`c877343`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/c877343a1bc7994f2bffd8cba88006bfddd65cc2))

* misc. ([`47a1c58`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/47a1c58413967dfe346e331677658fd490e7483b))

* misc. ([`cc03bcb`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/cc03bcbaefe8313b522d8ab6198b210b51744bf8))

* misc. ([`9e5f776`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/9e5f776dad634b8de14d100e318f6d82d1ec0a31))

* dev: mount shared dir for ankicard generation ([`f872ed0`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/f872ed0e21e2f5848552290a695978cf06bb3826))

* dev: remove unneeded install in dockerfile ([`ed6f51c`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/ed6f51c8f1957701fc0084b93b765ea0a297c272))

* dev: update cruft (#191)

Auto-created ([`e6fd14d`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/e6fd14d75d29d09dba84042e9d8045c51008c903))

* Merge pull request #190 from MartinBernstorff/mbern_dependent-flamingo

ci: add arm64 to deploy ([`f2529bc`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/f2529bc5b1112df0959bf1abd58b54c879e8901a))

* Update readme.md ([`6ec8a1a`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/6ec8a1a5cddb1b6d7327abcb56338a0b18b676e8))

* Merge pull request #177 from MartinBernstorff/mb/fix_deploy

ci: update docker build action ([`a11a7c2`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/a11a7c253d1b96a4aa69c576a9995f006fc2ee79))

* Update readme.md ([`0a0b577`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/0a0b57711d59bfadae504f546b7345aa9c913162))

* Update readme.md ([`b8e5041`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/b8e50417740f8907ca091f58eb35c30fb904f4c6))

* Merge branch &#39;main&#39; into mb/fix_deploy ([`9e27591`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/9e275919f68e1ba7b172f315ea1c2124aafa5fb8))


## v0.5.1 (2023-10-28)

### Fix

* fix: docker deploy should be lowercase ([`56d0517`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/56d0517da01ba25c950e5c01e13e190fd4bbeabe))

### Unknown

* Merge pull request #176 from MartinBernstorff/mb/fix_deploy

fix: docker deploy should be lowercase ([`be9b35d`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/be9b35d84405b0067e6b4caed08fa8c8e92a2eeb))

* Update readme.md ([`25c38cc`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/25c38cc1135e8027d2158014942c40c2bfd18e63))


## v0.5.0 (2023-10-28)

### Ci

* ci: add docker deploy ([`a658f15`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/a658f15e9818449262f123ddc63d6ae64e1b4bbe))

* ci: support multiline comment ([`273d2c9`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/273d2c980b67e0b12a52246e1d98e1144cc5111a))

* ci: remove unused section ([`79bb2d2`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/79bb2d21327e243398ffbe56a17055e9e44f4b10))

* ci: make integration test unique ([`85753df`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/85753df8d6270f53fa85eaf8496e456e0efb5631))

* ci: build prod image as part of tests ([`b595956`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/b59595611de1bc208501cdb09c630d20cfbc7728))

### Documentation

* docs: update contribution ([`a804fc7`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/a804fc7627e330cfa21fc92c0a0c360d0da88175))

* docs: update readme ([`704ae21`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/704ae21840118a826d0e8a4d3ce38e93e8a261fe))

### Feature

* feat: add integration test ([`e0526b6`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/e0526b60bfb06f2e0d75d0c52ebb8d1ed5d7966c))

* feat: add prod docker image ([`ed5f350`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/ed5f35099d7d79295726967545b6bce87b0927d2))

### Unknown

* Merge pull request #175 from MartinBernstorff/add-prod-dockerfile

feat: add prod dockerfile ([`99a6795`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/99a679573a927bbc7c8ca0854b0288f95593d67c))

* misc: type ignores ([`7e89279`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/7e89279b0dda4ccac8f1f0d5d8d9dd9755de87ad))

* Update readme.md ([`37dafbc`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/37dafbc394c4e08e801ff1e2b1f211d992ac045a))

* Update readme.md ([`5126fc0`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/5126fc082eea65de81b1e677c6ba64451dd55d84))


## v0.4.0 (2023-10-27)

### Feature

* feat: add build command ([`d6cb133`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/d6cb1330cbc7b7fbc4babc2e9e480da6a37bb5b0))

### Fix

* fix: duplicate version toml ([`8526eed`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/8526eed202a59021c15b258fcdf422172f7972b7))

### Unknown

* Merge pull request #174 from MartinBernstorff/mb/critical-mockingbird

feat: add build command ([`94af2bf`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/94af2bf7c8a178c476adbc553774b64f22b78aab))


## v0.3.0 (2023-10-27)

### Build

* build: auto-fix formatting by default ([`16806cf`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/16806cfb1d5caa54f41626148dd6d779405fbf44))

* build: update tasks.py ([`cef2666`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/cef266634fecb9546ccd149b53d3116f81764bb5))

* build: typo ([`c3b4ed0`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/c3b4ed0e1bccc0f72abec5d60d8a13c2d1d5c983))

* build: more informative messaging when syncing ([`d351a16`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/d351a169c723f524e96ebe8c6618c4881097ab24))

* build: pull before push ([`027d426`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/027d426159a89893249e698a8a00b38c60a7761c))

* build: hide result from gh pr lsit ([`9c91fa1`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/9c91fa19cf96d944d4c7ed8ace8f4fd42677e665))

* build: only open browser if PR does not exist ([`883ddca`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/883ddca4bdb160ce809e161d4d17345d7927e7d7))

* build: prettier messages ([`4c5d961`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/4c5d96153067b555571d05834cd1541ed1249b6a))

* build: hide output of branch_exists_on_remote ([`9bef312`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/9bef31295b03348c52649193d3fc6129cffedc08))

* build: separate exist and does not exist flow ([`b044fe6`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/b044fe67b9b523c0644a0bebf2ab710ee47ddc4d))

* build: remove @task decorator from utils function ([`2e7a61d`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/2e7a61d46d39b45dc0d7cf37c966733f2de5bdc6))

* build: add timeout to pr list ([`d76f8d1`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/d76f8d1f840385130fb4b8e89b325a8955371483))

* build: fix quotation marks ([`d833bc5`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/d833bc599dd3139d2d5539485a7e0c2599cbda65))

* build: push branch to origin if doesn&#39;t exist ([`2b07dd9`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/2b07dd9f3c63033fc6a9abe35f36017b9b900fdc))

* build: push to PR if exists ([`137aa06`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/137aa0616c0e2f6409becf47ab8c88c0bf6d9ab6))

* build: ask for commit if uncommitted changes before PR ([`4b4f7d3`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/4b4f7d39d316e7d920ea637279241f175a28f065))

* build: complete migration to Invoke ([`4c77a87`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/4c77a87fe1b1cc50581991b4c1698cc7953b8d89))

* build: use all available cores ([`f9916e8`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/f9916e8147819a47642a157900305bc56e4bf149))

* build: add more emojis ([`bb858f9`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/bb858f9bd191316997990219531f392b3e2f795d))

* build: make tests only show minimal effect ([`65c3ddc`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/65c3ddcf80afc187de6192e4c6d20f44329ac61d))

* build: run failed tests first ([`af11fcb`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/af11fcbadb72778574257f8163915cea13e159c3))

* build: missing backslash ([`0fa130e`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/0fa130e9fb611b3795f1dfeba8b306191a4c523d))

* build: pre_commit before mypy ([`d2a5c40`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/d2a5c4008945e3f8e532987d04be009b65de9bfb))

* build: misc. ([`968cd47`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/968cd4713f315ad77b0d1516cf18903fa5a9ecfe))

* build: misc. ([`0d94a1d`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/0d94a1df383e873ccc71cbf48494bc8931ceab8d))

* build: first makefile ([`e446e8b`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/e446e8b61ec74ecf14308a685e9fea406339174a))

* build: remove unused readme ([`7f00c19`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/7f00c19a6635e0168ae16126b40d7db6db1611d7))

### Chore

* chore: cleanup repo ([`2f7c31f`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/2f7c31f97139275964d034da616f7d8ca1ad5c79))

### Ci

* ci: update cruft ([`28c6125`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/28c61258104da50093e9762387c8e50269112c9f))

* ci: run release after tests ([`345abc3`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/345abc37ad64191113de7b9afac81a001170059d))

* ci: create hosts before push ([`6d38c59`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/6d38c59ba3b38d3a71c09d2ea08cecfc84dd4a64))

* ci: update cruft ([`357ac0a`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/357ac0a10ad7409b5d725d8c03ed8669cec0032b))

* ci: reenable release ([`6a81185`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/6a81185f68c81d5b0ac23369c480687015f4acb0))

* ci: reenable release ([`1d2d20a`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/1d2d20affac9d21f9f376a37c3836c6c918fca0d))

* ci: re-enable caching in tests ([`dee7316`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/dee7316908ab7d8ffbcf813500943af622f6a7c6))

* ci: move dependencies to correct subheading ([`fea7ee1`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/fea7ee1f89829974fa8bee49f9724b5848fe093f))

* ci: invalidate cache ([`4eb6aae`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/4eb6aaef43e2df931b56de953cb5f9b847a8ccd7))

* ci: run tests ([`26473be`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/26473bef39f6acf0fd2fd7d7f2441544f8678954))

* ci: simplify ([`abae734`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/abae734e498eedc95537e2579101f56e32d75a26))

* ci: remove pull-request template ([`bfbe55d`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/bfbe55d2241c9ec260e0d2b9d762e30443f453bb))

* ci: use nimble-python ([`9da7e6c`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/9da7e6cc0d4e45fd7abf1d2536ed59be76215fb6))

* ci: create pr on web ([`654349a`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/654349a36bab5bd1ef9015a572dab176fcdecb09))

* ci: send alert if script fails ([`25f88c2`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/25f88c2773a55b1a1fa8ac20cf4793f85cf116ae))

* ci: add dockerignore ([`35f6ecf`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/35f6ecfc8cb47be58b75246fc16a8954c43b0acb))

* ci: align dockerfile devcontainer python with rest of project ([`fd0a59d`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/fd0a59d97bc3e72c5ad1e22c1349e3168012eb04))

* ci: install pre-commit hooks on setup ([`61bfc12`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/61bfc1257ec01476c331cf2d6e586268aed2b121))

* ci: optimise layers for deps ([`eea7e9b`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/eea7e9b6412071dae6dc6b2f28af73cf93307047))

* ci: install test deps in dev container ([`0a03465`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/0a034657ff9ed42a8a4727c37115d45b2c1a9e56))

* ci: do not automatically commit formatting changes ([`9073d12`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/9073d12f21ba7cec2bc178c997005fa33598654b))

* ci: update tasks ([`2837861`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/283786145c625efd9e942d090a06fa05b977c978))

* ci: print branch name ([`3e3dbf2`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/3e3dbf247e79c196896239c1b6f3103d750f9831))

* ci: update cruft ([`4e5a414`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/4e5a414bc3af76b690806c9acc47b343e3c5faa2))

* ci: update paths ([`29cc8ce`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/29cc8cea1aaa789f69b48b89a34fe8e8b3c94f2c))

* ci: remove unused PR ([`949e2e3`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/949e2e312b75ed38541e0354518bd8753e96d034))

* ci: simplify call ([`c072a29`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/c072a294bd354f45b491a896e9fda18cf329e566))

* ci: update tasks ([`687cdb8`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/687cdb8dec71d5a1a21a8f91cbbf412a5239393c))

* ci: broader ignore for venv ([`a5f534f`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/a5f534f83c434da9c18e92495d3bf3c7e2e3c0cb))

* ci: minimal test interface ([`0059b80`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/0059b803ead752006d1943b06b351d8591324fad))

* ci: update cruft ([`bda3461`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/bda3461e914fcd421b2fcc9107f267a98734bff5))

* ci: update cruft ([`169171c`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/169171ce0677d21e9559784f99deb811d2b536b4))

* ci: disable release ([`a73a8d3`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/a73a8d3827e0d918c09e66852c54efa824fa31a3))

* ci: update cruft ([`382231d`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/382231db184585973869738e581f9f2323e8fead))

* ci: remove poetry ([`a7c091d`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/a7c091d668eab47f24fccfd708b02a115fa3a1e1))

* ci: update cruft ([`9a3c0fb`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/9a3c0fb10b7d9e258aa6df00e0d621f101c8b380))

* ci: add mypy to pre-commit ([`9746c27`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/9746c2722e862159844fe10c22cb8ac68e7f79c0))

### Documentation

* docs: improve readme ([`b5a4ccc`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/b5a4ccc2684f1fc55ab02608fd9b8cf9f92fb607))

* docs: update docs ([`d0b646d`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/d0b646df07910a25e357d24d6554ca2e1a7f2674))

* docs: clean up readme ([`bcf2480`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/bcf2480cf1eb3a2532338d82e27f7ad6b02b1658))

### Feature

* feat: bump ([`26ea9fb`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/26ea9fb53ac4693a834b3c2fd65846e8850fb43d))

* feat: use functionalpy ([`b7352f1`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/b7352f1961177661ce7de8b5f4c5a754564140dd))

* feat: use functionalpy ([`72d106a`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/72d106a5e9597798f329d502401c4d4848a9721d))

* feat: add docker image ([`2c0b7c6`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/2c0b7c6e3233f235c2b5fee1c8f0deeb6558a9f3))

* feat: pre-populate msic ([`73dcb46`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/73dcb46273e88509ae4fb872c979d2ab1144635d))

* feat: add preferred extensions ([`388dce3`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/388dce336c8fc8497da338729c6cb34727137dfc))

* feat: add dev_container ([`0e29b4d`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/0e29b4dbe41a6df5728026db66e22fb1a56ed988))

* feat: dynamic user dir in debug main launch.json ([`0aa5d38`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/0aa5d386d073a8e3d77c3a5957f6beb45fed6f31))

* feat: robustness to cards with errors ([`d340b50`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/d340b50f1bf5bae9f49794e86dfd65d46d893a99))

* feat: add vscode setting sto tracking ([`147716e`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/147716e164d13a1474001905ac24d4465446e974))

* feat: use obsidian uris ([`e107087`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/e1070871474f9205fd905d0e33a6e5e374ae0143))

* feat: support dash in links ([`add5191`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/add51919ccd246d84225b5989b3f04a6b110b858))

* feat: restrict polling time ([`00f163e`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/00f163ea912b35278fa0f3fdf6ec18b88c632b13))

* feat: improve dir parsing speed ([`e17dea6`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/e17dea693d268eeebeedbe83125a3b1e2f81aef2))

* feat: update guid for qa ([`f88d7ad`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/f88d7ad44e9ddc3dbe181c9f8866257d9b308090))

* feat: add guid test for qa ankinotes ([`dfdf04c`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/dfdf04cf962cdb906427f9339eeadb18256583bf))

* feat: add Obsidian URI to AnkiCards ([`b04f44b`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/b04f44b89db5df81de2ba2a805899a48f88c0ee8))

* feat: sync deletions ([`14c24e2`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/14c24e21cb09d34ecb7aefc95f535b815e02cda2))

* feat: delete cards on sync ([`cfd82c9`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/cfd82c968a39c3ba82341d04c39d1f9fc3f90019))

* feat: add support for markdown link aliases ([`add7e2a`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/add7e2ac3769ad99b0bb8841a93fa21af4718ba3))

* feat: add tts ([`5eaf984`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/5eaf9848937678588b84213acbb81a663f6e1d5d))

* feat: attempt tts addition ([`3ccb493`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/3ccb49365eec003ce98bb6ae1c3e0a7f491ff7b7))

* feat: decrease length of note id ([`6075894`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/6075894de68d34b5a2db7277bf82d9aba604c798))

### Fix

* fix: correctly sync dirs in bind mounts ([`3e269ee`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/3e269ee2dfceb005b7418336cf0f3a5d821c3027))

* fix: add field to attribute, not property ([`274370f`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/274370f914078c8c8b00bd1cc42fe26bacce2f2f))

* fix: re-add required import ([`3d0d51d`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/3d0d51d5354ce31ddbc18d3d3fa662635cc38933))

* fix: infinite loop ([`ce7470a`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/ce7470a08570d14a5d6667a3b08f989d302936b6))

* fix: pin invoke to version 2.1.0 ([`a5c56b9`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/a5c56b946ae5083cf67aaed0dd51c0876ad61b7c))

* fix: incorrect type hints from misaka ([`6988e7a`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/6988e7a63957a9f23c4b8296b44b64768e798ea2))

* fix: remove rej ([`152f124`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/152f124d4bb608f041da4b53dcd34666803b84c5))

* fix: typo ([`e687c3e`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/e687c3ed239ea8abdabf06143657c5a2a9a5f577))

* fix: overlapping commands ([`dd66cc1`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/dd66cc11ceda6b1890b1c69a11e36578f515b2da))

* fix: do not point to non-existing license ([`5197292`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/5197292ddd6b30e549cd46167a89495a29623a88))

* fix: shrink matching ([`5dc43d7`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/5dc43d7b62752affc4a9d3ee73fc723084727472))

* fix: remove da references ([`1b32634`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/1b326345dfa2ce65814a4412c91bd67e59354f85))

### Refactor

* refactor: major rewrite of input pipeline ([`88793cd`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/88793cd886c444e4cbe2e3dd55d010ff33590b78))

* refactor: split ankicard into AnkiQA and AnkiCloze ([`824660c`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/824660c165e70be08d0d4992ac69f4a400b9cf28))

* refactor: specify anki packagegenerator ([`8b52a42`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/8b52a42c32e443188684fe825894d636dc3e4083))

* refactor: extract url generation ([`b740700`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/b7407001d357a5e814394effaa5bd45a4b9c130b))

* refactor: modularise ([`5eba16c`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/5eba16ceefb68fb8b6a5a0ec6f68897716fe2db2))

* refactor: split cards_to_decks ([`fa183f0`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/fa183f08bc883a81bf41fd94beb0d9765e04053b))

* refactor: renaming ([`61baacc`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/61baacc5d6374dff99f4707887afce02d040a1d0))

* refactor: split git sync and github pr handling ([`981d105`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/981d105a222b2f90c61adbb1a6d71a2ead1dee8a))

* refactor: remove unused arguments from config ([`c27068b`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/c27068bb735cae85c8d85b1353ab3181e76b6b75))

* refactor: remove support for QA DK card ([`125c725`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/125c725a23cdf68f6a5edd317ec6a863665500a7))

### Style

* style: Auto-fixes from pre-commit ([`45d16ee`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/45d16eea207f5a337de8878f82dfd9a28657e402))

* style: Auto-fixes from pre-commit ([`8c79758`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/8c7975885265bce9de1a9919fcb929e841e8862c))

* style: lint ([`1998401`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/19984014599e94f84ff46d128de126feb05e9818))

* style: linting ([`2db1686`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/2db1686bcf4a4e09b87cbdaf5605efc9f2ad879f))

* style: linting ([`98f0a06`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/98f0a0604de83de09d33922ebbd61986bdde6bf7))

* style: linting ([`521cf42`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/521cf42889a64bd8c3de873657643b03e0a0e483))

* style: linting ([`1b59dcc`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/1b59dccd5bfc4d59cfca8a05bb7f4144671460c7))

* style: remove unused type: ignore ([`0fb4b28`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/0fb4b28d598a16e91ea7db562eafaeff05ef01eb))

* style: linting ([`6198058`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/6198058164273d63d4de0dc597854915b5a90d75))

* style: linting ([`17c3163`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/17c31631ce35ed2c03dcf87247f0f69e5476980a))

### Unknown

* Merge pull request #173 from MartinBernstorff/mb/critical-mockingbird

ci: update cruft ([`ebcef8c`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/ebcef8c3b3e358003b64e42f9ee95acb654cbd97))

* major: bump ([`2062688`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/20626889259f3365f9936dfa64004745f263427d))

* Merge pull request #172 from MartinBernstorff/mb/melted-gull

ci: run release after tests ([`51a0e48`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/51a0e487056a0c2cc6596af9dd2eee2cd1e2cbd4))

* Merge pull request #170 from MartinBernstorff/mb/cultural-goldfish

ci: reenable release ([`ac0e0c1`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/ac0e0c1cfd16a24c6980499fadb751701cc3f13b))

* misc. ([`255e288`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/255e2888d11ade7975dccde1285f98b335335349))

* Merge pull request #169 from MartinBernstorff/mb/external-landfowl

ci: re-enable caching in tests ([`5751833`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/5751833d8f3d14d15074febff6cc501f10589f3a))

* Merge pull request #168 from MartinBernstorff/mb/necessary-swallow

ci: use nimble-python ([`65a46f4`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/65a46f4e9536b55d1414d4a59d883f92b47ff11c))

* cruft updates ([`6d496b5`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/6d496b529babb615a3a5cce46d7c63be35562cea))

* misc. ([`7e97a06`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/7e97a067abe21d860ed92c858985c0b4b36bb165))

* misc. ([`e512c5b`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/e512c5b3cdc393d792cbc2c814d9a70864f7d402))

* types: ignore unknown types ([`40cc8e6`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/40cc8e69d74327a2ce50acc657a361a653ae34d3))

* misc. ([`01ec648`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/01ec6484cce41b46b382fb0bd544a0e6f27b018e))

* format: line length ([`249592b`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/249592b84bf608fecbb22b8f8142ca41a4572b01))

* ruff: format ([`804b6b8`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/804b6b82cad5af6db744cd347def2d63f683959a))

* format: remove unused imports ([`082ea88`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/082ea8844e9ad1abfbad18fa122e47c1f2aea768))

* cleanup ([`413edea`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/413edea11b6d2a04e02bb6401a34441a6988077c))

* Merge pull request #165 from MartinBernstorff/mb/fix_bind_mounts

fix: bind mounts ([`3217d85`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/3217d85671d687efb8dd388f84d0f30175d7affd))

* Merge branch &#39;main&#39; into mb/fix_bind_mounts ([`3d6fded`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/3d6fded0de4e48aac694a918f0724488fb116539))

* misc. ([`f91f319`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/f91f319e46935ce423489d49289f8715fa5c13b4))

* Merge pull request #163 from MartinBernstorff/mb/debug_no_such_file_or_directory

fix: correct bind mounts ([`7984cd2`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/7984cd28fa9f487d111e6bb8af3e21c24f063aef))

* misc. ([`0773a19`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/0773a1918843b03b147edc14dc779c7da6e73647))

* Merge pull request #159 from MartinBernstorff/2

v2 ([`ff5fd40`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/ff5fd40d9d5dbb95f25f0cb3ad4a350e9323b6ae))

* v2 ([`58bbcae`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/58bbcaed0bd69ace73dd63ee68e2262034c67027))

* Merge pull request #157 from MartinBernstorff/MartinBernstorff-patch-2

Update readme.md ([`f843f48`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/f843f48db2f8384c3098e853ca991689e069bf67))

* Update readme.md ([`96eaa92`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/96eaa920d31321d4f1c8fbd9e6597b4d321c1edb))

* Merge pull request #156 from MartinBernstorff/mb/create_prod_docker_image

create prod docker image ([`ab2e688`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/ab2e688cfa5f632653c90e915810beb55a6763fa))

* misc. ([`d013219`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/d013219a37065a971b91d6f1615f555a9fbece12))

* misc. ([`38d7eb9`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/38d7eb9e1fdf195739004eb3c22844b20f47f795))

* misc. ([`4e79feb`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/4e79feb0e959aa05cabde66a2f4ceadb0114ea2f))

* misc. ([`70b63e9`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/70b63e92cd23e4183303e3bd89404f4787a9ab84))

* remove dev container json to enable local mounts ([`8dd1c66`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/8dd1c6680aefe8a8b35fa28c0ab4872cd071a137))

* git: ignore input mount ([`967a745`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/967a7459d06c5e7d59c7f19fd775694fd7b4422d))

* dev: do not add mount by default ([`670cef6`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/670cef6941ffd02e4629926a07d756dfa37b3558))

* misc. ([`2aa9395`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/2aa93953d6b23bc9253299e27c21e359b3cec3e9))

* remove unused docopt and centralise globals ([`8668bdd`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/8668bdda30959f2175e04d503b88230ca174e47c))

* misc. ([`939b1d9`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/939b1d9a5d3b2fcb23e19da4658bfbeff43db4d0))

* Merge pull request #150 from MartinBernstorff/mb/simplify_deps

simplify deps ([`c888a4c`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/c888a4cccaed7853beb9776d66dd6b3b87b2da7b))

* deps: pytest-sugar version ([`0a05976`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/0a05976897f5b1b5df715bb2fca0061d0fb127b0))

* pytest-xdist deps ([`580bdcd`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/580bdcd614c9df1a0e3159f30b86999e0a973f18))

* Merge branch &#39;main&#39; into mb/simplify_deps ([`979b421`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/979b42170531096050025fdffa4db6b8915b5a98))

* simplify deps ([`35c70d7`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/35c70d741d22d93859869ac42e308c48ab70aeaa))

* Merge pull request #148 from MartinBernstorff/mb/add_monitoring

add monitoring ([`e0ad96f`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/e0ad96fde8425040784605c783043d9745337e1c))

* correct sentry version ([`fa14c24`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/fa14c24900f99ec3a8f3feb2f76c52d32d0351d0))

* Merge branch &#39;main&#39; into mb/add_monitoring ([`f6a584a`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/f6a584a06db7f411caa9ba58c439bf562c8d30b7))

* Merge pull request #149 from MartinBernstorff/mb/migrate_ci_to_use_dev_container

misc. ([`19255eb`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/19255eb27e48f50526da99c2b1a9e691bd50ef1b))

* Benchmark with prebuilt image ([`f2d3e80`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/f2d3e80705540a0bee34bd3b475a50db87dd5fdf))

* rename validation job ([`3dfefa5`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/3dfefa5a79bab037fa992994a977d5dff7d1a1b1))

* another typo ([`6d332b8`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/6d332b80c639443a791c2a7e99d9310b0cf73747))

* fix type in dev container image spec ([`5d83095`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/5d83095ca334f830f965810fd4fee49ca639e849))

* simplify ci ([`12ab185`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/12ab185b22af6f0f0109f9147cf895ac632e8c59))

* add gh cli to devcontainer.json ([`9ed6b15`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/9ed6b15eb71173be5f5e9a3cfe6ae4f499ae6604))

* python3 .10 ([`c780ae4`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/c780ae4499f4189a5fb2b317e04111eb6b5410a3))

* dev: simplify dev container ([`8b90fb1`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/8b90fb1f916b55d8c61445497a75d8dc579360f4))

* misc. ([`8778915`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/87789153b1975aa391564d2a130b4893c783e984))

* Merge remote-tracking branch &#39;origin/main&#39; into mb/add_monitoring ([`748d415`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/748d4150c9a9343244081394083e5125c3ee54f6))

* dev: push changes on succesful tests ([`55c2589`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/55c2589d21488f945d7211b36bdf63ee5a2ce7f2))

* types: fix ([`18dfb85`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/18dfb8526b9504756502f41f381af43ee224dd1c))

* dev: add type-checks to make ([`228e951`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/228e95124b8ff57f3f9c6dd74f64eab36da689e7))

* dev: add makefile tools ([`b52e2a8`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/b52e2a8a2e8f3b756a2ef20a398af61a5178d474))

* dev: add makefile ([`0a8f043`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/0a8f043b0d3fc80ed7375cf824e83b62fbb2482e))

* add black as provider ([`34aa978`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/34aa978ef44274bbad18af0d63a9c5cab2babc44))

* add sentry monitoring ([`ea59872`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/ea598720dc544d954b33dc3ba1544d755b7b3a2f))

* Merge pull request #147 from MartinBernstorff/mb/feat_add_shell_script_logging

add shell script logging ([`fcaca78`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/fcaca7878bf8b8ab5b3dcc00414f90ddc99b550e))

* add shell script logging ([`fa7fb28`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/fa7fb284d14290cdad86bd0bc50ef095c45d6828))

* Merge pull request #146 from MartinBernstorff/dependabot/pip/pyright-1.1.330.post0

deps:(deps-dev): bump pyright from 1.1.329 to 1.1.330.post0 ([`09e7a26`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/09e7a268d2b8377da1608c0a061e42a4b4f6c478))

* deps:(deps-dev): bump pyright from 1.1.329 to 1.1.330.post0

Bumps [pyright](https://github.com/RobertCraigie/pyright-python) from 1.1.329 to 1.1.330.post0.
- [Release notes](https://github.com/RobertCraigie/pyright-python/releases)
- [Commits](https://github.com/RobertCraigie/pyright-python/compare/v1.1.329...v1.1.330.post0)

---
updated-dependencies:
- dependency-name: pyright
  dependency-type: direct:production
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`5cdeb83`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/5cdeb83a9564fe853913f5b4b1ff88afa952b1df))

* Merge pull request #139 from MartinBernstorff/mb/feat_add_devcontainer

ci: add devcontainer ([`9d0635f`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/9d0635f301a5e881e1c7f865b63f06250d248f47))

* container: ensure lazygit does not show pop-up every time ([`ad0f51d`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/ad0f51d8fbfcb673e3ce7ef9c352cce5ad6e7ac4))

* Merge branch &#39;main&#39; into mb/feat_add_devcontainer ([`98a8763`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/98a8763c644907c2c2917ae2c15caffceba8051e))

* misc. ([`37f3d8b`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/37f3d8b336aeccf148556da367387b7d6c702e28))

* misc. ([`b3eb9eb`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/b3eb9eb4631b0f94ea6080cb602616884950b3c8))

* Merge pull request #140 from MartinBernstorff/dependabot/pip/pyright-1.1.329

deps:(deps-dev): bump pyright from 1.1.327 to 1.1.329 ([`c77656f`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/c77656fae7f75612dd82713b971f55fa6991b32b))

* deps:(deps-dev): bump pyright from 1.1.327 to 1.1.329

Bumps [pyright](https://github.com/RobertCraigie/pyright-python) from 1.1.327 to 1.1.329.
- [Release notes](https://github.com/RobertCraigie/pyright-python/releases)
- [Commits](https://github.com/RobertCraigie/pyright-python/compare/v1.1.327...v1.1.329)

---
updated-dependencies:
- dependency-name: pyright
  dependency-type: direct:production
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`a48366e`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/a48366e932c7792df02f3e6f628feee085498e5e))

* cleanup ([`156cc84`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/156cc84d08d10a928c9259d49337cc6d599a2936))

* Merge pull request #138 from MartinBernstorff/dependabot/pip/pyright-1.1.327

deps:(deps-dev): bump pyright from 1.1.326 to 1.1.327 ([`9f4be02`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/9f4be02a99f26b01b197540ac038fa3c7e735c1a))

* deps:(deps-dev): bump pyright from 1.1.326 to 1.1.327

Bumps [pyright](https://github.com/RobertCraigie/pyright-python) from 1.1.326 to 1.1.327.
- [Release notes](https://github.com/RobertCraigie/pyright-python/releases)
- [Commits](https://github.com/RobertCraigie/pyright-python/compare/v1.1.326...v1.1.327)

---
updated-dependencies:
- dependency-name: pyright
  dependency-type: direct:production
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`ac56d47`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/ac56d475b8781303e40f40df962db9d724545b79))

* Merge pull request #137 from MartinBernstorff/dependabot/pip/pyright-1.1.326

deps:(deps-dev): bump pyright from 1.1.325 to 1.1.326 ([`494de01`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/494de01a5e897c4e6f8c07dbe36cd1a99c351f1d))

* Merge pull request #136 from MartinBernstorff/dependabot/pip/furo-gte-2022.12.7-and-lt-2023.9.11

deps:(deps-dev): update furo requirement from &lt;2023.8.20,&gt;=2022.12.7 to &gt;=2022.12.7,&lt;2023.9.11 ([`faa8888`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/faa8888410d38af2651c41f23de49efbbfd36f4c))

* deps:(deps-dev): bump pyright from 1.1.325 to 1.1.326

Bumps [pyright](https://github.com/RobertCraigie/pyright-python) from 1.1.325 to 1.1.326.
- [Release notes](https://github.com/RobertCraigie/pyright-python/releases)
- [Commits](https://github.com/RobertCraigie/pyright-python/compare/v1.1.325...v1.1.326)

---
updated-dependencies:
- dependency-name: pyright
  dependency-type: direct:production
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`78fcd9d`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/78fcd9ddc169f09cde76c6c189f46527e939079e))

* deps:(deps-dev): update furo requirement

Updates the requirements on [furo](https://github.com/pradyunsg/furo) to permit the latest version.
- [Release notes](https://github.com/pradyunsg/furo/releases)
- [Changelog](https://github.com/pradyunsg/furo/blob/main/docs/changelog.md)
- [Commits](https://github.com/pradyunsg/furo/compare/2022.12.07...2023.09.10)

---
updated-dependencies:
- dependency-name: furo
  dependency-type: direct:production
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`cdf0bcf`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/cdf0bcfc8517e119e18b862bae5dc882bfab9c20))

* Merge pull request #132 from MartinBernstorff/mb/rewrite_entrypoint

refactor: rewrite entrypoint ([`8e68c36`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/8e68c3662792d4430b2201ba27e3cf6366a55e3a))

* deps: pin invoke version ([`02b1549`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/02b1549e7e4904109eade91f41fa5f03e4d044d4))

* deps: pin invoke ([`a1d6339`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/a1d6339305ad2eb1048bf887083e0128a0536cc5))

* formatting ([`0ff68d0`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/0ff68d0617e53644b0aefb9721bbd24555e63aa5))

* Merge pull request #135 from MartinBernstorff/dependabot/pip/pyright-1.1.325

deps:(deps-dev): bump pyright from 1.1.324 to 1.1.325 ([`36587bf`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/36587bf0a0417a3c8f4ebb1eefe2cfbf59a3f2b9))

* deps:(deps-dev): bump pyright from 1.1.324 to 1.1.325

Bumps [pyright](https://github.com/RobertCraigie/pyright-python) from 1.1.324 to 1.1.325.
- [Release notes](https://github.com/RobertCraigie/pyright-python/releases)
- [Commits](https://github.com/RobertCraigie/pyright-python/compare/v1.1.324...v1.1.325)

---
updated-dependencies:
- dependency-name: pyright
  dependency-type: direct:production
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`8e92745`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/8e92745079b9cb84d099570aeb09de941a68a297))

* Merge branch &#39;main&#39; into mb/rewrite_entrypoint ([`b857f27`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/b857f27b43bf6c860c8bed37e1bbbdbe5dfd5b7d))

* Merge pull request #131 from MartinBernstorff/mb/debug

feat: dynamic user dir in debug main launch.json ([`68a68f2`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/68a68f2b33a5eeffb76f70561153c1c55efa9a5e))

* Merge pull request #134 from MartinBernstorff/dependabot/pip/invoke-2.2.0

deps:(deps-dev): bump invoke from 2.1.0 to 2.2.0 ([`ed9446a`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/ed9446a12f2a4291afcf5083e13fc96fb49a793c))

* Merge pull request #133 from MartinBernstorff/dependabot/pip/pyright-1.1.324

deps:(deps-dev): bump pyright from 1.1.323 to 1.1.324 ([`8eea198`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/8eea198a766e9d511ae5949e4e67090f4957c16e))

* deps:(deps-dev): bump invoke from 2.1.0 to 2.2.0

Bumps [invoke](https://github.com/pyinvoke/invoke) from 2.1.0 to 2.2.0.
- [Commits](https://github.com/pyinvoke/invoke/compare/2.1.0...2.2.0)

---
updated-dependencies:
- dependency-name: invoke
  dependency-type: direct:production
  update-type: version-update:semver-minor
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`08026a6`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/08026a63f7f9bb5757a499780a2c447384ce9b29))

* deps:(deps-dev): bump pyright from 1.1.323 to 1.1.324

Bumps [pyright](https://github.com/RobertCraigie/pyright-python) from 1.1.323 to 1.1.324.
- [Release notes](https://github.com/RobertCraigie/pyright-python/releases)
- [Commits](https://github.com/RobertCraigie/pyright-python/compare/v1.1.323...v1.1.324)

---
updated-dependencies:
- dependency-name: pyright
  dependency-type: direct:production
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`d567ab5`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/d567ab5d70640604c45b8425ba91eb113f0eeb5f))

* misc. ([`1df62e9`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/1df62e963d1b66942046254150235865d5d95626))

* auto-style ([`cf4bf99`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/cf4bf99daa9928869fce518533b6aef1e13fa154))

* Merge pull request #130 from MartinBernstorff/mb/debug

Mb/debug ([`9946429`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/9946429c33aff2164e4287d2d4f11a08fd0a1390))

* deps: lock invoke version ([`7cdbca5`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/7cdbca566963ef5c44bdfe2e7d24578f49b16f23))

* Merge pull request #127 from MartinBernstorff/dependabot/pip/sphinx-gte-5.3.0-and-lt-7.3.0

deps:(deps-dev): update sphinx requirement from &lt;7.2.0,&gt;=5.3.0 to &gt;=5.3.0,&lt;7.3.0 ([`45ba02e`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/45ba02e9c702897192921438e13b4e1616258d44))

* deps:(deps-dev): update sphinx requirement

Updates the requirements on [sphinx](https://github.com/sphinx-doc/sphinx) to permit the latest version.
- [Release notes](https://github.com/sphinx-doc/sphinx/releases)
- [Changelog](https://github.com/sphinx-doc/sphinx/blob/master/CHANGES)
- [Commits](https://github.com/sphinx-doc/sphinx/compare/v5.3.0...v7.2.2)

---
updated-dependencies:
- dependency-name: sphinx
  dependency-type: direct:production
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`53731c9`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/53731c9c8fae2c124595d41dcee791dc2b9448de))

* Merge pull request #129 from MartinBernstorff/dependabot/pip/pyright-1.1.323

deps:(deps-dev): bump pyright from 1.1.322 to 1.1.323 ([`56b57c0`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/56b57c033bbc5c27416b5aa4021a2dd655e4203b))

* Merge pull request #128 from MartinBernstorff/dependabot/pip/furo-gte-2022.12.7-and-lt-2023.8.20

deps:(deps-dev): update furo requirement from &lt;2023.7.27,&gt;=2022.12.7 to &gt;=2022.12.7,&lt;2023.8.20 ([`784838d`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/784838de2fbe17db07a18ff91d8ad5e6669e39c7))

* deps:(deps-dev): bump pyright from 1.1.322 to 1.1.323

Bumps [pyright](https://github.com/RobertCraigie/pyright-python) from 1.1.322 to 1.1.323.
- [Release notes](https://github.com/RobertCraigie/pyright-python/releases)
- [Commits](https://github.com/RobertCraigie/pyright-python/compare/v1.1.322...v1.1.323)

---
updated-dependencies:
- dependency-name: pyright
  dependency-type: direct:production
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`e8019f9`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/e8019f95bb6ac1a001b7e58fd89d97258b66f2f7))

* deps:(deps-dev): update furo requirement

Updates the requirements on [furo](https://github.com/pradyunsg/furo) to permit the latest version.
- [Release notes](https://github.com/pradyunsg/furo/releases)
- [Changelog](https://github.com/pradyunsg/furo/blob/main/docs/changelog.md)
- [Commits](https://github.com/pradyunsg/furo/compare/2022.12.07...2023.08.19)

---
updated-dependencies:
- dependency-name: furo
  dependency-type: direct:production
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`afe01a6`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/afe01a60f4cb7d1b0bd429496b68681e01978f8d))

* Merge pull request #126 from MartinBernstorff/dependabot/pip/pyright-1.1.322

deps:(deps-dev): bump pyright from 1.1.320 to 1.1.322 ([`4e66ebd`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/4e66ebd0c917ec4ffbaa8ba19387c2a4f582558e))

* Merge pull request #125 from MartinBernstorff/dependabot/pip/invoke-2.2.0

deps:(deps-dev): bump invoke from 2.1.0 to 2.2.0 ([`69de660`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/69de660f076bac0af53eaa51c51ad68a2c3b2d58))

* deps:(deps-dev): bump pyright from 1.1.320 to 1.1.322

Bumps [pyright](https://github.com/RobertCraigie/pyright-python) from 1.1.320 to 1.1.322.
- [Release notes](https://github.com/RobertCraigie/pyright-python/releases)
- [Commits](https://github.com/RobertCraigie/pyright-python/compare/v1.1.320...v1.1.322)

---
updated-dependencies:
- dependency-name: pyright
  dependency-type: direct:production
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`a38d24f`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/a38d24f25723447dc2151d05be52cda3511b2f12))

* deps:(deps-dev): bump invoke from 2.1.0 to 2.2.0

Bumps [invoke](https://github.com/pyinvoke/invoke) from 2.1.0 to 2.2.0.
- [Commits](https://github.com/pyinvoke/invoke/compare/2.1.0...2.2.0)

---
updated-dependencies:
- dependency-name: invoke
  dependency-type: direct:production
  update-type: version-update:semver-minor
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`e4da95d`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/e4da95d139cd029992b1ee82e668e6d6b4ca98c1))

* Merge pull request #124 from MartinBernstorff/MartinBernstorff-patch-2

Update readme.md ([`4b6f694`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/4b6f6948fdb6fb5e0dce7d7c2fc20c862226645d))

* Update readme.md ([`f1327d8`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/f1327d852456d7e81d3f9e04e12f0f045af43711))

* Merge pull request #123 from MartinBernstorff/mb/split_ankicard_into_two

mb/split ankicard into two ([`db3c8f4`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/db3c8f4ae214fee46f79d01beadaddbc9b2793df))

* Merge pull request #122 from MartinBernstorff/MartinBernstorff-patch-3

Update readme.md ([`496263e`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/496263e552aa60f97c905ac5ef76d26e588ebf51))

* Merge pull request #121 from MartinBernstorff/MartinBernstorff-patch-2

Update readme.md ([`68e1495`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/68e149516ba58c3a05b2b27835211bd6d5464e91))

* style ([`9f17cea`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/9f17cea3aaffba5534417d7462ba3bd6824018f6))

* Update readme.md ([`5551251`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/55512516615aad916cb71e4147274cd14ff05423))

* Update readme.md ([`8d8835f`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/8d8835fef063b5edbca32f151ae2a40b2e4e598e))

* Merge pull request #120 from MartinBernstorff/mb/update_readme

docs: improve readme ([`05b88c8`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/05b88c8d6f1a2cb4201a1a25120dfbc31a4b428e))

* Merge branch &#39;main&#39; into mb/update_readme ([`69aa28f`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/69aa28f075652157b0f57471f088329c0695e4d8))

* Merge pull request #119 from MartinBernstorff/mb/rename

refactor: specify anki packagegenerator ([`a1a3ac8`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/a1a3ac8a6c2b9b525b96b76d3494ad698242b056))

* Merge pull request #118 from MartinBernstorff/mb/further_decompose_ankicard

mb/further decompose ankicard ([`546ab2f`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/546ab2ffedade5bdac2ffb7876fc404727966792))

* missing import ([`008dce0`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/008dce0beb9604575f806b63355bbb38c8297786))

* Merge pull request #117 from MartinBernstorff/mb/refactor_object

mb/refactor object ([`b272769`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/b272769494995e1908e16eb402db7907cd89b12c))

* --a ([`94f58d6`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/94f58d607c83406f17b113018579e7dcbe733afd))

* misc. ([`08ae3f7`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/08ae3f7f48ceeb3636c10127b6b6c0ccf1f1336f))

* refactor ([`e6a609b`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/e6a609bfb24f14b2fcebc1b43060d5c32acf10f6))

* use any venv ([`2d37c65`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/2d37c65aa3abeaf29c935ab1580dd4a231bffe11))

* Merge pull request #116 from MartinBernstorff/mb/add_line_numbers

Mb/add line numbers ([`e165d33`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/e165d33161aa4ecaf561170da8dcd5a3ad783664))

* fix off-by-one error on line numbers ([`3df1d53`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/3df1d53b5fb8043b775cb9113ab017c57dcb6ba9))

* update anki_card url with line number ([`225e6a5`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/225e6a5f216fb61d8c6cbea1f976da4e28db2902))

* add line numbers to qa prompts ([`f086157`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/f0861574cb132c3c272b183a6d19422194a8b8cc))

* Merge pull request #115 from MartinBernstorff/mb/add_visualisation_to_readme

add visualisation to readme ([`66f1f26`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/66f1f26b99f536623deae9bbe5e6b8282aca305d))

* add visualisation to readme ([`f8541e8`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/f8541e88ab67a3a78c2734c663ccf42a6de03d90))

* Merge pull request #114 from MartinBernstorff/mb/move_to_obsidian

feat: use obsidian uris ([`2162d85`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/2162d85d1776edd4da77dce807bcd875020148da))

* Merge pull request #113 from MartinBernstorff/mb/feat_support_dash_in_link

Mb/feat support dash in link ([`f85f93f`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/f85f93f8f152741c569b8dfc893a8103d487ab51))

* Merge pull request #111 from MartinBernstorff/dependabot/pip/pyright-1.1.320

deps:(deps-dev): bump pyright from 1.1.318 to 1.1.320 ([`03ecf58`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/03ecf5837c728397c0458264a8030f4b5939968d))

* Merge pull request #112 from MartinBernstorff/dependabot/pip/invoke-2.2.0

deps:(deps-dev): bump invoke from 2.1.0 to 2.2.0 ([`7a72969`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/7a7296978df65a9bc1e27260f126160b58bdf654))

* deps:(deps-dev): bump invoke from 2.1.0 to 2.2.0

Bumps [invoke](https://github.com/pyinvoke/invoke) from 2.1.0 to 2.2.0.
- [Commits](https://github.com/pyinvoke/invoke/compare/2.1.0...2.2.0)

---
updated-dependencies:
- dependency-name: invoke
  dependency-type: direct:production
  update-type: version-update:semver-minor
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`a324e65`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/a324e6541a049288b0989452b6f8074c85fc71cb))

* deps:(deps-dev): bump pyright from 1.1.318 to 1.1.320

Bumps [pyright](https://github.com/RobertCraigie/pyright-python) from 1.1.318 to 1.1.320.
- [Release notes](https://github.com/RobertCraigie/pyright-python/releases)
- [Commits](https://github.com/RobertCraigie/pyright-python/compare/v1.1.318...v1.1.320)

---
updated-dependencies:
- dependency-name: pyright
  dependency-type: direct:production
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`3dd0320`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/3dd0320548714afa06429b15bc6cf4dd4af5be10))

* Merge pull request #110 from MartinBernstorff/mb/fix_alias_parsing_with_parens

Mb/fix alias parsing with parens ([`5179086`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/5179086aefb54a6ca947d443c39726cfa2dd5941))

* cleanup ([`30bc8e9`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/30bc8e9c6b16299e96e1b6c7571909d6d62aea4e))

* Merge pull request #108 from MartinBernstorff/feat-restrict-anki-polling-time
Feat restrict anki polling time

- [ ] I have considered whether this PR needs review, and requested a review if necessary.

Fixes issue #

# Notes for reviewers
Reviewers can skip X, but should pay attention to Y.

&lt;!-- {BearID:a96da1b7c406e5e2a5d1b5cd5401d005} --&gt; ([`b01cbae`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/b01cbae9ac3b81296d9314a8ccd90b541b7ec453))

* Merge pull request #108 from MartinBernstorff/feat-restrict-anki-polling-time

Feat restrict anki polling time ([`37962a8`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/37962a897eccf34d50291a064dbff01fbe3de3c1))

* Merge branch &#39;main&#39; of https://github.com/martbern/personal-mnemonic-medium ([`65f1470`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/65f1470276f0a016d03d73991815ecc7211a706f))

* Merge pull request #107 from MartinBernstorff/mb/improve_dir_parsing_speed

feat: improve dir parsing speed ([`98e24b4`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/98e24b4528ecab05d1ed152aabb2c8700722d796))

* Merge remote-tracking branch &#39;origin/mb/improve_dir_parsing_speed&#39; ([`7bf1690`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/7bf1690f87addb28ebecd630501dea720aa9627d))

* Merge branch &#39;main&#39; into mb/improve_dir_parsing_speed ([`995be12`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/995be12e68656ec83567ca88821b9dad031bb79d))

* Merge pull request #106 from MartinBernstorff/mb/skip_medicine

feat: skip medicine deck ([`979f742`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/979f742e11320a85b25133d69a8ab708830b0fd2))

* --a ([`5048d91`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/5048d911e9d353952a4c42ebde854a932c4192ad))

* --a ([`b969bf8`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/b969bf86861d01364b4c02b62eb30fbec2b59264))

* --a ([`ca74f43`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/ca74f43f13d82bc002d8e6e8a8a2c3476f9f59d1))

* Merge remote-tracking branch &#39;origin/main&#39; into mb/skip_medicine ([`bf8ab51`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/bf8ab513d797ceb2711cc1c8184119340225889a))

* skip medicine deck ([`edf376c`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/edf376c4272a0c105a224f0cac3b469f5ffe1525))

* Merge pull request #105 from MartinBernstorff/mb/only_sync_if_modified_in_ded

feat: only sync if notes modified ([`467ec7a`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/467ec7ac5d9de5228dd2ad660052c64559293626))

* fix type hints ([`c73fb22`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/c73fb22a4e0e7dca152d501da0e69d0f4fbbb929))

* Merge branch &#39;main&#39; into mb/only_sync_if_modified_in_ded ([`44ca1ab`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/44ca1ab7578166dc25fd3390bd155d0f0df27ad2))

* only sync if notes modified ([`ef450b0`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/ef450b06e670435187bd3e97d41205cc698d95bb))

* Merge pull request #104 from MartinBernstorff/feat_continous_polling

continuous polling ([`b83652d`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/b83652d8ff6d7d760952578e45a5f9ea97a17c8a))

* continuous polling ([`d33b781`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/d33b7814c1d86149105702bedc5cf7d219d429c9))

* Merge pull request #103 from MartinBernstorff/mb/fix_guid_addition

fix: guid on QA cards ([`8b275f1`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/8b275f1ba89a53cc611437e093863d349c2f0a9d))

* deps: pin invoke to 2.1.0 to avoid errors as values ([`ce274c2`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/ce274c2dd3ae949e5709af5e7e182d622a83a716))

* --a ([`85fb429`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/85fb42982515330eb5aa829f7c666d770f9beee4))

* Merge pull request #101 from MartinBernstorff/dependabot/pip/furo-gte-2022.12.7-and-lt-2023.7.27

deps:(deps-dev): update furo requirement from &lt;2023.5.21,&gt;=2022.12.7 to &gt;=2022.12.7,&lt;2023.7.27 ([`a73899e`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/a73899eac9192eca646950a06343db69a50a0544))

* deps:(deps-dev): update furo requirement

Updates the requirements on [furo](https://github.com/pradyunsg/furo) to permit the latest version.
- [Release notes](https://github.com/pradyunsg/furo/releases)
- [Changelog](https://github.com/pradyunsg/furo/blob/main/docs/changelog.md)
- [Commits](https://github.com/pradyunsg/furo/compare/2022.12.07...2023.07.26)

---
updated-dependencies:
- dependency-name: furo
  dependency-type: direct:production
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`5a48d69`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/5a48d690999127ba0516880c3329335f8d1e85d8))

* Merge pull request #102 from MartinBernstorff/dependabot/pip/sphinx-design-gte-0.3.0-and-lt-0.5.1

deps:(deps-dev): update sphinx-design requirement from &lt;0.3.1,&gt;=0.3.0 to &gt;=0.3.0,&lt;0.5.1 ([`8b0005a`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/8b0005af6697ff97d2202f2cf61fe7dc02453921))

* Merge pull request #100 from MartinBernstorff/dependabot/pip/sphinx-gte-5.3.0-and-lt-7.2.0

deps:(deps-dev): update sphinx requirement from &lt;7.1.0,&gt;=5.3.0 to &gt;=5.3.0,&lt;7.2.0 ([`9dbeda4`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/9dbeda4dbb268c6e8e6bc88581e261667741d814))

* deps:(deps-dev): update sphinx-design requirement

Updates the requirements on [sphinx-design](https://github.com/executablebooks/sphinx-design) to permit the latest version.
- [Release notes](https://github.com/executablebooks/sphinx-design/releases)
- [Changelog](https://github.com/executablebooks/sphinx-design/blob/main/CHANGELOG.md)
- [Commits](https://github.com/executablebooks/sphinx-design/compare/v0.3.0...v0.5.0)

---
updated-dependencies:
- dependency-name: sphinx-design
  dependency-type: direct:production
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`949014a`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/949014a7795537a125e842ee9c9e5e68194eae5f))

* deps:(deps-dev): update sphinx requirement

Updates the requirements on [sphinx](https://github.com/sphinx-doc/sphinx) to permit the latest version.
- [Release notes](https://github.com/sphinx-doc/sphinx/releases)
- [Changelog](https://github.com/sphinx-doc/sphinx/blob/master/CHANGES)
- [Commits](https://github.com/sphinx-doc/sphinx/compare/v5.3.0...v7.1.1)

---
updated-dependencies:
- dependency-name: sphinx
  dependency-type: direct:production
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`c22a7db`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/c22a7dbb18a4772440742b336a53409d12f6cb02))

* Merge pull request #99 from MartinBernstorff/dependabot/pip/pyright-1.1.318

deps:(deps-dev): bump pyright from 1.1.317 to 1.1.318 ([`94e1bc7`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/94e1bc7bf26afb3a36f96e64164d041b095348f2))

* deps:(deps-dev): bump pyright from 1.1.317 to 1.1.318

Bumps [pyright](https://github.com/RobertCraigie/pyright-python) from 1.1.317 to 1.1.318.
- [Release notes](https://github.com/RobertCraigie/pyright-python/releases)
- [Commits](https://github.com/RobertCraigie/pyright-python/compare/v1.1.317...v1.1.318)

---
updated-dependencies:
- dependency-name: pyright
  dependency-type: direct:production
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`59b7374`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/59b737429a8049cb00b83ef4fd99623b7991bc19))

* Merge pull request #98 from MartinBernstorff/dependabot/pip/pyright-1.1.317

deps:(deps-dev): bump pyright from 1.1.316 to 1.1.317 ([`87c4e00`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/87c4e005e3889fa89e38a0cf8833cfee4e6cc920))

* Merge pull request #97 from MartinBernstorff/dependabot/pip/invoke-2.2.0

deps:(deps-dev): bump invoke from 2.1.3 to 2.2.0 ([`1321c31`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/1321c31856157016dee0a8118bb3d6c03244bf05))

* deps:(deps-dev): bump pyright from 1.1.316 to 1.1.317

Bumps [pyright](https://github.com/RobertCraigie/pyright-python) from 1.1.316 to 1.1.317.
- [Release notes](https://github.com/RobertCraigie/pyright-python/releases)
- [Commits](https://github.com/RobertCraigie/pyright-python/compare/v1.1.316...v1.1.317)

---
updated-dependencies:
- dependency-name: pyright
  dependency-type: direct:production
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`9899673`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/98996739e09c2c68722adc9fdd08673c51294237))

* deps:(deps-dev): bump invoke from 2.1.3 to 2.2.0

Bumps [invoke](https://github.com/pyinvoke/invoke) from 2.1.3 to 2.2.0.
- [Commits](https://github.com/pyinvoke/invoke/compare/2.1.3...2.2.0)

---
updated-dependencies:
- dependency-name: invoke
  dependency-type: direct:production
  update-type: version-update:semver-minor
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`22bd718`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/22bd71848b39610df63ae0f79c5abfb094d86b9d))

* Merge pull request #96 from MartinBernstorff/mb/sync_deletion

Mb/sync deletion ([`48ae41e`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/48ae41e190250111cdc36153a6fa8cdac06b2c2c))

* Merge branch &#39;main&#39; into mb/sync_deletion ([`1b230ae`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/1b230aeeec32c77cb92623fcbd6827ecaec0e409))

* styling ([`a2e553e`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/a2e553e74ef081b614f734c0a355a5ddf2982daa))

* Merge pull request #95 from MartinBernstorff/dependabot/pip/pyright-1.1.316

deps:(deps-dev): bump pyright from 1.1.314 to 1.1.316 ([`e854fe6`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/e854fe61bb1ffc25e58cc803e33eaec3b5611f26))

* deps:(deps-dev): bump pyright from 1.1.314 to 1.1.316

Bumps [pyright](https://github.com/RobertCraigie/pyright-python) from 1.1.314 to 1.1.316.
- [Release notes](https://github.com/RobertCraigie/pyright-python/releases)
- [Commits](https://github.com/RobertCraigie/pyright-python/compare/v1.1.314...v1.1.316)

---
updated-dependencies:
- dependency-name: pyright
  dependency-type: direct:production
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`d6e375c`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/d6e375c6712a912032654d444b75fd2e40cd4bbf))

* Merge pull request #94 from MartinBernstorff/dependabot/pip/invoke-2.1.3

deps:(deps-dev): bump invoke from 2.1.2 to 2.1.3 ([`ddf971c`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/ddf971c909f34372a81cc260e6ca1e1c5abf653f))

* Merge pull request #93 from MartinBernstorff/dependabot/pip/pyright-1.1.314

deps:(deps-dev): bump pyright from 1.1.313 to 1.1.314 ([`7af94ff`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/7af94ff54c4bb5164785a0f2c5313c4880dc1993))

* deps:(deps-dev): bump invoke from 2.1.2 to 2.1.3

Bumps [invoke](https://github.com/pyinvoke/invoke) from 2.1.2 to 2.1.3.
- [Commits](https://github.com/pyinvoke/invoke/compare/2.1.2...2.1.3)

---
updated-dependencies:
- dependency-name: invoke
  dependency-type: direct:production
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`8fbac68`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/8fbac68516e74180a96e68ad86f0c051f3f6940e))

* deps:(deps-dev): bump pyright from 1.1.313 to 1.1.314

Bumps [pyright](https://github.com/RobertCraigie/pyright-python) from 1.1.313 to 1.1.314.
- [Release notes](https://github.com/RobertCraigie/pyright-python/releases)
- [Commits](https://github.com/RobertCraigie/pyright-python/compare/v1.1.313...v1.1.314)

---
updated-dependencies:
- dependency-name: pyright
  dependency-type: direct:production
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`ae99f7d`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/ae99f7d50e417dc34c0aca2cef5f4aecf844f265))

* Merge pull request #92 from MartinBernstorff/dependabot/pip/invoke-2.1.2

deps:(deps-dev): bump invoke from 2.1.1 to 2.1.2 ([`1ba428f`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/1ba428f3196e00a327306d23cd9ec2516ac63aef))

* Merge pull request #91 from MartinBernstorff/dependabot/pip/pyright-1.1.313

deps:(deps-dev): bump pyright from 1.1.305 to 1.1.313 ([`ddbbd06`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/ddbbd060f5f74d7debcc8de6f39ff08dfbd7b390))

* deps:(deps-dev): bump invoke from 2.1.1 to 2.1.2

Bumps [invoke](https://github.com/pyinvoke/invoke) from 2.1.1 to 2.1.2.
- [Commits](https://github.com/pyinvoke/invoke/compare/2.1.1...2.1.2)

---
updated-dependencies:
- dependency-name: invoke
  dependency-type: direct:production
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`8e1a14f`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/8e1a14fe3ed2882057bbec95c98626727c3fc79f))

* deps:(deps-dev): bump pyright from 1.1.305 to 1.1.313

Bumps [pyright](https://github.com/RobertCraigie/pyright-python) from 1.1.305 to 1.1.313.
- [Release notes](https://github.com/RobertCraigie/pyright-python/releases)
- [Commits](https://github.com/RobertCraigie/pyright-python/compare/v1.1.305...v1.1.313)

---
updated-dependencies:
- dependency-name: pyright
  dependency-type: direct:production
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`2127536`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/21275367d0fca3a0e1847433921dc7714e7ad4e3))

* Merge pull request #90 from MartinBernstorff/MartinBernstorff-patch-2

Update readme.md ([`010e6f9`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/010e6f9bfa4420dd5dd83cff54de6af0dda9075c))

* Update readme.md ([`c5f37a1`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/c5f37a1e43a08e4b433ba342f6547449441fead6))

* --a ([`7e7eda7`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/7e7eda72f086ad8c5717d3b64182bbac7ab616fa))

* --a ([`8702130`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/87021307bb0b3c82c1e035f3f10c506f25c552b1))

* Merge pull request #89 from MartinBernstorff/MartinBernstorff-patch-2

Update readme.md ([`743a946`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/743a946a8dcfd94034b408938d98f735eecb8880))

* Update readme.md ([`2747360`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/2747360e572e632ed1aecc9b6b01a8dc122bcd35))

* Merge pull request #88 from MartinBernstorff/mb/sync_deletion

feat: sync deletion ([`98c07f2`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/98c07f2d3b3baeeacc209109c3ee4ae5b4bf1ef1))

* misc. ([`47e63d4`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/47e63d49af7e0cd1cc3de47fd32db416f4fe0d09))

* misc. ([`ee622e5`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/ee622e57ad69001349eb9687125f019beac1767d))

* misc. ([`0c0134d`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/0c0134d8b7b792cab330ee711c85b978b8182dc5))

* misc. ([`bba22a7`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/bba22a78e87e2aca6483fef083575fe27d0d813e))

* misc. ([`d8ab4ef`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/d8ab4eff5ca6db6eeaf02397848272113d284a52))

* --a ([`d2b59da`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/d2b59da96532e3f6014ee556de1c59eab4aafd7c))

* misc. ([`bcf0169`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/bcf01693288f3d34f44937cd0eefec033e48eb58))

* merge ([`18bddc6`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/18bddc656986eac884d3c82563a0d16165b39b5c))

* tests: fix tests ([`12cbe19`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/12cbe1913f6280a0d4ff0e7bd1cbb87631ca93ba))

* --a ([`8630858`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/86308589dcc17e25af50155b558c85c203cf4cd3))

* tests: adapt to new card_uuid property ([`fe72a2e`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/fe72a2e7ca0b6603e7e9ad61ed0a3410ca8b6235))

* misc. ([`bdb9009`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/bdb9009882351e5e563454a3d27c26d0ffb5f444))

* misc. ([`7eea28c`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/7eea28c03bef9d9b32c816094c9c1f8144bd1683))

* misc ([`64f1822`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/64f1822743c09c2608af0aef56b4176d5bb5c33e))

* Merge pull request #87 from MartinBernstorff/dependabot/pip/ruff-0.0.270

deps:(deps-dev): bump ruff from 0.0.269 to 0.0.270 ([`e1c22e1`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/e1c22e17dea78a7b9b1702b299e6e196105332f2))

* Merge pull request #85 from MartinBernstorff/dependabot/pip/types-pyyaml-6.0.12.10

deps:(deps-dev): bump types-pyyaml from 6.0 to 6.0.12.10 ([`3f4c223`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/3f4c22399aacc3bb7b2c802afecae09b00f76957))

* Merge pull request #86 from MartinBernstorff/dependabot/pip/pytest-cov-gte-3.0.0-and-lt-4.2.0

deps:(deps-dev): update pytest-cov requirement from &lt;4.1.0,&gt;=3.0.0 to &gt;=3.0.0,&lt;4.2.0 ([`6ecbf67`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/6ecbf676c0acae63c401fc28512ba0c106686175))

* deps:(deps-dev): bump ruff from 0.0.269 to 0.0.270

Bumps [ruff](https://github.com/charliermarsh/ruff) from 0.0.269 to 0.0.270.
- [Release notes](https://github.com/charliermarsh/ruff/releases)
- [Changelog](https://github.com/charliermarsh/ruff/blob/main/BREAKING_CHANGES.md)
- [Commits](https://github.com/charliermarsh/ruff/compare/v0.0.269...v0.0.270)

---
updated-dependencies:
- dependency-name: ruff
  dependency-type: direct:production
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`569694f`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/569694f91adc9e59f6e59a211874ef96b279e6ae))

* deps:(deps-dev): update pytest-cov requirement

Updates the requirements on [pytest-cov](https://github.com/pytest-dev/pytest-cov) to permit the latest version.
- [Changelog](https://github.com/pytest-dev/pytest-cov/blob/master/CHANGELOG.rst)
- [Commits](https://github.com/pytest-dev/pytest-cov/compare/v3.0.0...v4.1.0)

---
updated-dependencies:
- dependency-name: pytest-cov
  dependency-type: direct:production
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`01f4cb2`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/01f4cb230c896284d1b3f39afda8c79e4b7a161a))

* deps:(deps-dev): bump types-pyyaml from 6.0 to 6.0.12.10

Bumps [types-pyyaml](https://github.com/python/typeshed) from 6.0 to 6.0.12.10.
- [Commits](https://github.com/python/typeshed/commits)

---
updated-dependencies:
- dependency-name: types-pyyaml
  dependency-type: direct:production
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`1762e04`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/1762e047daf85a06bb54b6ba15034f06b7b8ea35))

* Merge pull request #83 from MartinBernstorff/dependabot/pip/ruff-0.0.269

deps:(deps-dev): bump ruff from 0.0.267 to 0.0.269 ([`fcb632d`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/fcb632d5aa74d6a00c806892f6fe99a1db7de1f6))

* deps:(deps-dev): bump ruff from 0.0.267 to 0.0.269

Bumps [ruff](https://github.com/charliermarsh/ruff) from 0.0.267 to 0.0.269.
- [Release notes](https://github.com/charliermarsh/ruff/releases)
- [Changelog](https://github.com/charliermarsh/ruff/blob/main/BREAKING_CHANGES.md)
- [Commits](https://github.com/charliermarsh/ruff/compare/v0.0.267...v0.0.269)

---
updated-dependencies:
- dependency-name: ruff
  dependency-type: direct:production
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`a6dcd82`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/a6dcd825cef18447aeff76e0f9da3a1e5c176454))

* Merge pull request #84 from MartinBernstorff/dependabot/pip/furo-gte-2022.12.7-and-lt-2023.5.21

deps:(deps-dev): update furo requirement from &lt;2022.12.8,&gt;=2022.12.7 to &gt;=2022.12.7,&lt;2023.5.21 ([`229fdf4`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/229fdf495398e658dc80e0fa43558f72ede3c445))

* Merge pull request #82 from MartinBernstorff/dependabot/pip/pre-commit-3.3.2

deps:(deps-dev): bump pre-commit from 3.3.1 to 3.3.2 ([`ae02f4b`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/ae02f4b144131a942c9e4220d3365563eb77e6f9))

* deps:(deps-dev): update furo requirement

Updates the requirements on [furo](https://github.com/pradyunsg/furo) to permit the latest version.
- [Release notes](https://github.com/pradyunsg/furo/releases)
- [Changelog](https://github.com/pradyunsg/furo/blob/main/docs/changelog.md)
- [Commits](https://github.com/pradyunsg/furo/compare/2022.12.07...2023.05.20)

---
updated-dependencies:
- dependency-name: furo
  dependency-type: direct:production
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`d18cfcc`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/d18cfcc3ae183a7d62c58af9a2213b3f36d46767))

* deps:(deps-dev): bump pre-commit from 3.3.1 to 3.3.2

Bumps [pre-commit](https://github.com/pre-commit/pre-commit) from 3.3.1 to 3.3.2.
- [Release notes](https://github.com/pre-commit/pre-commit/releases)
- [Changelog](https://github.com/pre-commit/pre-commit/blob/main/CHANGELOG.md)
- [Commits](https://github.com/pre-commit/pre-commit/compare/v3.3.1...v3.3.2)

---
updated-dependencies:
- dependency-name: pre-commit
  dependency-type: direct:production
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`b2b7667`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/b2b7667687a0549ca4d2dd5db958d1d7a3f05e8d))

* Merge pull request #81 from MartinBernstorff/dependabot/pip/ruff-0.0.267

deps:(deps-dev): bump ruff from 0.0.265 to 0.0.267 ([`afb40bb`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/afb40bb6c6bd6cf8810d6fb801cdfc32f3835089))

* Merge pull request #80 from MartinBernstorff/dependabot/pip/pytest-xdist-gte-3.0.0-and-lt-3.4.0

deps:(deps-dev): update pytest-xdist requirement from &lt;3.3.0,&gt;=3.0.0 to &gt;=3.0.0,&lt;3.4.0 ([`6beebe3`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/6beebe3a5b9c8dabca4840059f1b7f458c05bc8c))

* deps:(deps-dev): bump ruff from 0.0.265 to 0.0.267

Bumps [ruff](https://github.com/charliermarsh/ruff) from 0.0.265 to 0.0.267.
- [Release notes](https://github.com/charliermarsh/ruff/releases)
- [Changelog](https://github.com/charliermarsh/ruff/blob/main/BREAKING_CHANGES.md)
- [Commits](https://github.com/charliermarsh/ruff/compare/v0.0.265...v0.0.267)

---
updated-dependencies:
- dependency-name: ruff
  dependency-type: direct:production
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`d193516`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/d1935160a70e321a650137888726e43bc354f661))

* deps:(deps-dev): update pytest-xdist requirement

Updates the requirements on [pytest-xdist](https://github.com/pytest-dev/pytest-xdist) to permit the latest version.
- [Changelog](https://github.com/pytest-dev/pytest-xdist/blob/master/CHANGELOG.rst)
- [Commits](https://github.com/pytest-dev/pytest-xdist/compare/v3.0.0...v3.3.0)

---
updated-dependencies:
- dependency-name: pytest-xdist
  dependency-type: direct:production
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`50baf05`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/50baf05bbe55269cdaf271cb64b0f6c3a53f9104))

* Merge pull request #79 from MartinBernstorff/dependabot/pip/ruff-0.0.265

deps:(deps-dev): bump ruff from 0.0.262 to 0.0.265 ([`d0b078f`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/d0b078fc03250784d9a069514db64fa78db21d35))

* deps:(deps-dev): bump ruff from 0.0.262 to 0.0.265

Bumps [ruff](https://github.com/charliermarsh/ruff) from 0.0.262 to 0.0.265.
- [Release notes](https://github.com/charliermarsh/ruff/releases)
- [Changelog](https://github.com/charliermarsh/ruff/blob/main/BREAKING_CHANGES.md)
- [Commits](https://github.com/charliermarsh/ruff/compare/v0.0.262...v0.0.265)

---
updated-dependencies:
- dependency-name: ruff
  dependency-type: direct:production
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`6a863cb`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/6a863cbc6ddae27f345087a515bfbf194d525605))

* Merge pull request #78 from MartinBernstorff/dependabot/pip/pre-commit-3.3.1

deps:(deps-dev): bump pre-commit from 3.1.1 to 3.3.1 ([`db30bbc`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/db30bbc89bb13f7f7393d5b7a57ef95e02de27d0))

* deps:(deps-dev): bump pre-commit from 3.1.1 to 3.3.1

Bumps [pre-commit](https://github.com/pre-commit/pre-commit) from 3.1.1 to 3.3.1.
- [Release notes](https://github.com/pre-commit/pre-commit/releases)
- [Changelog](https://github.com/pre-commit/pre-commit/blob/main/CHANGELOG.md)
- [Commits](https://github.com/pre-commit/pre-commit/compare/v3.1.1...v3.3.1)

---
updated-dependencies:
- dependency-name: pre-commit
  dependency-type: direct:production
  update-type: version-update:semver-minor
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`59b49a3`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/59b49a37dc3f7adcbc5993c2a7d0e7a0b00b97a4))

* Merge pull request #76 from MartinBernstorff/dependabot/pip/sphinx-gte-5.3.0-and-lt-7.1.0

deps:(deps-dev): update sphinx requirement from &lt;6.3.0,&gt;=5.3.0 to &gt;=5.3.0,&lt;7.1.0 ([`43913e3`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/43913e3d5c1c0e69b13b1ed3f822e815d7a6a386))

* deps:(deps-dev): update sphinx requirement

Updates the requirements on [sphinx](https://github.com/sphinx-doc/sphinx) to permit the latest version.
- [Release notes](https://github.com/sphinx-doc/sphinx/releases)
- [Changelog](https://github.com/sphinx-doc/sphinx/blob/master/CHANGES)
- [Commits](https://github.com/sphinx-doc/sphinx/compare/v5.3.0...v7.0.0)

---
updated-dependencies:
- dependency-name: sphinx
  dependency-type: direct:production
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`9ff3ba1`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/9ff3ba1d6d8f9130dc21b704792468d05353f354))

* Merge pull request #75 from MartinBernstorff/dependabot/pip/ruff-0.0.262

deps:(deps-dev): bump ruff from 0.0.257 to 0.0.262 ([`c797266`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/c797266d36bf28e412b3ca5f2bbac79982c2b04a))

* deps:(deps-dev): bump ruff from 0.0.257 to 0.0.262

Bumps [ruff](https://github.com/charliermarsh/ruff) from 0.0.257 to 0.0.262.
- [Release notes](https://github.com/charliermarsh/ruff/releases)
- [Changelog](https://github.com/charliermarsh/ruff/blob/main/BREAKING_CHANGES.md)
- [Commits](https://github.com/charliermarsh/ruff/compare/v0.0.257...v0.0.262)

---
updated-dependencies:
- dependency-name: ruff
  dependency-type: direct:production
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`0f7f6b2`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/0f7f6b225d9d2deeca5b4aa8646444901c6eff81))

* Merge pull request #74 from MartinBernstorff/dependabot/pip/black-jupyter--23.3.0

deps:(deps-dev): bump black[jupyter] from 23.1.0 to 23.3.0 ([`7304b03`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/7304b038cadbf734c226f8be08a06aa9d0821a30))

* Merge pull request #73 from MartinBernstorff/dependabot/pip/sphinx-gte-5.3.0-and-lt-6.3.0

deps:(deps-dev): update sphinx requirement from &lt;6.2.0,&gt;=5.3.0 to &gt;=5.3.0,&lt;6.3.0 ([`94852e9`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/94852e9b6ef74d2d3523534735b8f4f64e3d28cd))

* deps:(deps-dev): bump black[jupyter] from 23.1.0 to 23.3.0

Bumps [black[jupyter]](https://github.com/psf/black) from 23.1.0 to 23.3.0.
- [Release notes](https://github.com/psf/black/releases)
- [Changelog](https://github.com/psf/black/blob/main/CHANGES.md)
- [Commits](https://github.com/psf/black/compare/23.1.0...23.3.0)

---
updated-dependencies:
- dependency-name: black[jupyter]
  dependency-type: direct:production
  update-type: version-update:semver-minor
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`04c566c`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/04c566c73b384f071cd172a63453b413809124c0))

* deps:(deps-dev): update sphinx requirement

Updates the requirements on [sphinx](https://github.com/sphinx-doc/sphinx) to permit the latest version.
- [Release notes](https://github.com/sphinx-doc/sphinx/releases)
- [Changelog](https://github.com/sphinx-doc/sphinx/blob/master/CHANGES)
- [Commits](https://github.com/sphinx-doc/sphinx/compare/v5.3.0...v6.2.0)

---
updated-dependencies:
- dependency-name: sphinx
  dependency-type: direct:production
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`6ba0468`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/6ba04687179f6449154ba94c9dc41f768a2f4bb6))

* Merge pull request #70 from MartinBernstorff/mb/update_cruft

build: update cruft ([`011d1ea`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/011d1eadb5b984b9c59538db296565dc12826109))

* Merge pull request #65 from MartinBernstorff/mb/update_paths

ci: update paths ([`bd1b6f5`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/bd1b6f522fd4ff3c582c53fd4030a8536eb826f9))

* Merge pull request #55 from MartinBernstorff/martbern/try_makefile

build: migrate to Invoke ([`3b0fcc1`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/3b0fcc1c64651972e6b08cbb72f39290334c0b07))

* Merge branch &#39;martbern/try_makefile&#39; of https://github.com/MartinBernstorff/personal-mnemonic-medium into martbern/try_makefile ([`3cb3529`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/3cb3529db244dab63c2002ea35dead3afacd54d3))

* Delete test.py ([`60aa58d`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/60aa58de74a1b2a1f4ea086cb45cb6c83b2ed622))

* misc. ([`34231f2`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/34231f2d7d5deaebd7d88dd17566dc6aa4869c80))

* tests: fix failing ([`1dee619`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/1dee6196439c4591d35843ad0eacbe568394d09d))

* misc. ([`04038f0`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/04038f0ef3de3704eabd5654a55765c7f9c304a7))

* misc. ([`54776e6`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/54776e68ba25247c05e05f16d90dface7b1935a3))

* bulid: misc ([`bd2f26e`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/bd2f26e8fdd7b7434801ada16f77444e3204c971))

* misc. changes ([`f4a0d81`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/f4a0d8104d839b29cb0c82d8db9d6d9667b015e8))

* Merge pull request #49 from MartinBernstorff/martbern/update_cruft_2

Martbern/update cruft 2 ([`8cf73d8`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/8cf73d81bf12b771da48e431e89a678f5947ff8d))

* deps:(deps-dev): bump ruff from 0.0.254 to 0.0.257

Bumps [ruff](https://github.com/charliermarsh/ruff) from 0.0.254 to 0.0.257.
- [Release notes](https://github.com/charliermarsh/ruff/releases)
- [Changelog](https://github.com/charliermarsh/ruff/blob/main/BREAKING_CHANGES.md)
- [Commits](https://github.com/charliermarsh/ruff/compare/v0.0.254...v0.0.257)

---
updated-dependencies:
- dependency-name: ruff
  dependency-type: direct:production
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`215672b`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/215672b4c2d5e9a12b9ad33f75b084ed06578c0d))

* Merge pull request #45 from MartinBernstorff/feat_support_markdown_link_alias

feat: support markdown link alias ([`4213e04`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/4213e047c9f371d2df643e46f319a71522f36cb9))

* Merge pull request #44 from MartinBernstorff/martbern/add_english_tts_to_qa

feat: add english tts to qa ([`e0eb897`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/e0eb897c73b3d9b55196ff7e4317cf075a24696b))

* dev: add pytypes yaml ([`a963f82`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/a963f8274239af34526aa0617f3a81cade52b779))

* Merge branch &#39;main&#39; into martbern/add_english_tts_to_qa ([`2538285`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/2538285ae37a66e5160c3c2c6ccc194c13dd015e))

* Merge pull request #42 from MartinBernstorff/update-cruft

update cruft ([`0c9e6c9`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/0c9e6c920bd76643546ea157709ba18544b1b8e2))

* Merge pull request #41 from MartinBernstorff/martbern/ci_disable_release

ci: disable release ([`4771735`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/47717352d83919e65e9146b2554176b36520373c))

* Merge pull request #39 from MartinBernstorff/martbern/update_docs

docs: update docs ([`731dfea`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/731dfeaa096a6e4b938de2945f2c7b8b8b194865))

* Merge pull request #40 from MartinBernstorff/update-cruft

update cruft ([`05cea4b`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/05cea4b4a91a131c243b234f329c31a2b757a86d))

* Merge pull request #34 from MartinBernstorff/martbern/update_cruft

ci: update cruft ([`13b4529`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/13b45293e5ba5e9f6b696c8be2379611cbe7708e))

* Merge pull request #33 from MartinBernstorff/dependabot/pip/sphinxext-opengraph-gte-0.7.3-and-lt-0.8.2

deps:(deps-dev): update sphinxext-opengraph requirement from &lt;0.7.4,&gt;=0.7.3 to &gt;=0.7.3,&lt;0.8.2 ([`3fc23fe`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/3fc23fe25c77fffd0082c4024e78027e8564e34f))

* deps:(deps-dev): update sphinxext-opengraph requirement

Updates the requirements on [sphinxext-opengraph](https://github.com/wpilibsuite/sphinxext-opengraph) to permit the latest version.
- [Release notes](https://github.com/wpilibsuite/sphinxext-opengraph/releases)
- [Commits](https://github.com/wpilibsuite/sphinxext-opengraph/compare/v0.7.3...v0.8.1)

---
updated-dependencies:
- dependency-name: sphinxext-opengraph
  dependency-type: direct:production
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`f79ce05`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/f79ce0562fe03ee1bc70a30a652ec118b92976a4))

* Merge pull request #32 from MartinBernstorff/martbern/decrease-length-of-note-id-hash

feat: decrease length of note id ([`87a3f7a`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/87a3f7a2dfce572488c12d7db8f1c829ed5bd9b8))


## v0.2.0 (2023-03-12)

### Ci

* ci: update cruft ([`89b9e86`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/89b9e8697ea20a53e44f4e511d91061e951b7013))

* ci: ignore bearimages ([`32bf9e4`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/32bf9e4069a575dda3ac45cd62e4b00608368525))

### Feature

* feat: exclude q. and a. fields from cloze prompts ([`5b2d6cd`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/5b2d6cda3825582381444b36c6ef1dbc8779d4af))

### Unknown

* Merge pull request #31 from MartinBernstorff/martbern/rewrite

Martbern/rewrite ([`285260a`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/285260a925c89477f0eeca7a26b4fca770cef259))

* Merge pull request #27 from MartinBernstorff/dependabot/pip/pytest-cov-gte-3.0.0-and-lt-4.1.0

deps:(deps-dev): update pytest-cov requirement from &lt;3.1.0,&gt;=3.0.0 to &gt;=3.0.0,&lt;4.1.0 ([`8fa46d1`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/8fa46d1a17ef57aacbb802a69ec84ce604370ac7))

* deps:(deps-dev): update pytest-cov requirement

Updates the requirements on [pytest-cov](https://github.com/pytest-dev/pytest-cov) to permit the latest version.
- [Release notes](https://github.com/pytest-dev/pytest-cov/releases)
- [Changelog](https://github.com/pytest-dev/pytest-cov/blob/master/CHANGELOG.rst)
- [Commits](https://github.com/pytest-dev/pytest-cov/compare/v3.0.0...v4.0.0)

---
updated-dependencies:
- dependency-name: pytest-cov
  dependency-type: direct:production
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`c1ec617`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/c1ec617bc6e4206fe6a51832cf310397a9ac6171))

* Merge pull request #30 from MartinBernstorff/dependabot/pip/black-23.1.0

deps:(deps-dev): bump black from 22.8.0 to 23.1.0 ([`37348e7`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/37348e70e90bcbe3429b60dfd02d4d867633cd77))

* Merge pull request #29 from MartinBernstorff/dependabot/pip/pre-commit-eq-3.1.1

deps:(deps-dev): update pre-commit requirement from &lt;2.21.0,==2.20.0 to ==3.1.1 ([`11ef695`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/11ef695ca9843e6dc619ef631833e5ea436b0827))

* deps:(deps-dev): bump black from 22.8.0 to 23.1.0

Bumps [black](https://github.com/psf/black) from 22.8.0 to 23.1.0.
- [Release notes](https://github.com/psf/black/releases)
- [Changelog](https://github.com/psf/black/blob/main/CHANGES.md)
- [Commits](https://github.com/psf/black/compare/22.8.0...23.1.0)

---
updated-dependencies:
- dependency-name: black
  dependency-type: direct:production
  update-type: version-update:semver-major
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`fa845b5`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/fa845b5374cc748fe872cc581d8191a0456bc975))

* Merge pull request #28 from MartinBernstorff/dependabot/pip/sphinx-gte-5.3.0-and-lt-6.2.0

deps:(deps-dev): update sphinx requirement from &lt;5.4.0,&gt;=5.3.0 to &gt;=5.3.0,&lt;6.2.0 ([`42fd015`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/42fd015727a1d34bbe25d89f37d1d0c0d07b9342))

* deps:(deps-dev): update pre-commit requirement

Updates the requirements on [pre-commit](https://github.com/pre-commit/pre-commit) to permit the latest version.
- [Release notes](https://github.com/pre-commit/pre-commit/releases)
- [Changelog](https://github.com/pre-commit/pre-commit/blob/main/CHANGELOG.md)
- [Commits](https://github.com/pre-commit/pre-commit/compare/v2.20.0...v3.1.1)

---
updated-dependencies:
- dependency-name: pre-commit
  dependency-type: direct:production
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`2dbe94e`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/2dbe94e39bae879d9389cf1962cf75b2727db092))

* deps:(deps-dev): update sphinx requirement

Updates the requirements on [sphinx](https://github.com/sphinx-doc/sphinx) to permit the latest version.
- [Release notes](https://github.com/sphinx-doc/sphinx/releases)
- [Changelog](https://github.com/sphinx-doc/sphinx/blob/master/CHANGES)
- [Commits](https://github.com/sphinx-doc/sphinx/compare/v5.3.0...v6.1.3)

---
updated-dependencies:
- dependency-name: sphinx
  dependency-type: direct:production
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`0ae2bc5`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/0ae2bc54607c40a268311fe070b151ce047e7469))

* Merge pull request #26 from MartinBernstorff/dependabot/pip/pytest-xdist-gte-3.0.0-and-lt-3.3.0

deps:(deps-dev): update pytest-xdist requirement from &lt;3.2.0,&gt;=3.0.0 to &gt;=3.0.0,&lt;3.3.0 ([`694732d`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/694732daef5e9ab519a553836df6c6c8d7a518fb))

* deps:(deps-dev): update pytest-xdist requirement

Updates the requirements on [pytest-xdist](https://github.com/pytest-dev/pytest-xdist) to permit the latest version.
- [Release notes](https://github.com/pytest-dev/pytest-xdist/releases)
- [Changelog](https://github.com/pytest-dev/pytest-xdist/blob/master/CHANGELOG.rst)
- [Commits](https://github.com/pytest-dev/pytest-xdist/compare/v3.0.0...v3.2.0)

---
updated-dependencies:
- dependency-name: pytest-xdist
  dependency-type: direct:production
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`9ee8c1e`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/9ee8c1e7f16574801b4599c839f51b8daaba7d75))


## v0.1.0 (2023-03-11)

### Chore

* chore: remove unused type ignore ([`4cbd2b8`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/4cbd2b88cc86c2d8ecc0716d15b64ef5596fa7de))

* chore: more typing ([`dcb04d0`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/dcb04d043ae173b02c6b86f707d4d24008d95241))

* chore: type everything ([`884deea`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/884deeaa9c5e58f5d82ade7cdad4575900b8f793))

* chore: housekeeping ([`3c93bd7`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/3c93bd738fbb122ba5d9f4babebeaa8ef9a9a391))

### Ci

* ci: update find comment ([`3de3a91`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/3de3a91015f316e5c651ef3f3de0e38704cf12fd))

* ci: update cruft logic ([`9d2109a`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/9d2109ac5d29195bb103a84e5cb8ebb08f7d07b0))

* ci: update cruft ([`aea9b87`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/aea9b870cd52a2d4784e98d11710971d19c6006b))

* ci: update cruft message ([`2343489`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/234348919d8f39546aadf1ff14de0873e30e9100))

* ci: update cruft failed template ([`2d793c5`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/2d793c53579cb2665039a35c11f13168b4f5b52c))

* ci: cruft ([`55b6232`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/55b62321376b3fee21252f4b2878f6e8bdaf2d4e))

* ci: cruft check ([`c3b5353`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/c3b5353b7febd1337acd3addc1a1711e47472bc5))

* ci: cruft ([`eca6564`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/eca65640591eeac6bd7edcb4aa6e3bdb3f450b80))

* ci: test new cruft procedure ([`e41862c`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/e41862c0433c7838282cd7e880dc6a3847c32f54))

* ci: test ([`62ea30c`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/62ea30c0e8d504409bd91fbdcd01540b99752268))

* ci: test ([`babf357`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/babf357b30cecd73e8c202a80d881cfd2c2399fa))

* ci: fix error in cruft ([`c3114e5`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/c3114e5809a7135ad7dabf088abc99cec35a0968))

* ci: try new cruft ci ([`6412ae8`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/6412ae8eaf9626de016abbef28e4c291e093c088))

* ci: update cruft ([`12bd8a9`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/12bd8a9736da761c405af7e42f0747073a1364bf))

* ci: permissions for setup_for_dev ([`8f23875`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/8f23875ad5e970bdb64503dc2a72a909e6c22e74))

### Feature

* feat: ignore cloze-likes in code blocks ([`80b0888`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/80b0888839ea8206fc1697674be4ac2e42e0627f))

* feat: compile fields to html ([`13f8c07`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/13f8c079a2db56c0b80161488d2831cc9d9eadf2))

* feat: better sh file ([`fc0b2e6`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/fc0b2e6197940906061e22f069c361d3f379685c))

* feat: working version ([`a8438c7`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/a8438c7b3cb42f4cb2718008b8e2ed4f2514c7ab))

* feat: migrate main to use new pipeline ([`fa71108`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/fa7110896aa326cf44646cb0fe7353c0d8ffa337))

* feat: create a unified pipeline ([`a703fcc`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/a703fcc8158d2412170dda333d24cc87bf4c3daf))

* feat: fit uuid generation to qa prompt extractor ([`4e33b0d`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/4e33b0d37075d897aba0a932316d10284572e1e4))

* feat: remove filepath requirement ([`65c97a5`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/65c97a5262965cd0776bfb36bc7108a27e83fd6d))

* feat: first working rewrite ([`9a16d98`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/9a16d983054fa03c005922778f1e4bc33222496d))

* feat: first stab at main package ([`069accd`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/069accdfff488ed285dabebdbb847fb1ba064c3b))

* feat: add markdown to card logic ([`f1a204f`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/f1a204ff74c898374f8399f34aba8577830391a0))

* feat: don&#39;t update bear ([`59fef60`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/59fef60eb4d22fc9e3e5443b7456a1687689d4e3))

* feat: add cloze extractor ([`8fda355`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/8fda355e9ab7b9e945c61c7b2853a3418cfa4458))

* feat: add source notes to QAPrompts ([`08bae17`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/08bae173fcd0ce96aa54319cbe529a918e0b3229))

* feat: add qa_prompt_extractor ([`377b426`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/377b426d97ab985832cb577cfbfa4e4c01d73fd6))

* feat: disable automatic tts (replaced by AwesomeTTS) ([`5f37882`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/5f37882a9ce24ba84e36b7d2d1939cc035144dbe))

### Fix

* fix: cruft typography ([`99b7a25`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/99b7a25ec613b8017309662354ed3def767975f3))

* fix: hash anki cards on markdown ([`b5a35b9`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/b5a35b91f58c3d43e237f495a30940e3ea780a00))

* fix: don&#39;t fail on missing media references ([`5274e3f`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/5274e3fb3f494c56c99624ec76cbbd307de548a4))

* fix: do not use tts for now ([`7e3bab5`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/7e3bab580adf7d50d556024db29dd343db6a8cb3))

* fix: typo in toml ([`be9499e`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/be9499e60f9e872112cedd6454ff6fa16af1eabe))

* fix: ensure guids match cloze ([`694f701`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/694f701aa44a1962168cb3256062f70371aef1cd))

* fix: match guide for first test case ([`ee41799`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/ee41799941a027792588821f22003fc2a4c99171))

* fix: better support for TTS ([`78032e7`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/78032e761e7661e1974d5595f39eaf43b8965264))

### Refactor

* refactor: add guards ([`c92eeb7`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/c92eeb7c101f7a3c30e57827b8d5e696c7c82b49))

* refactor: stylise pipeline ([`34ba2a3`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/34ba2a317f61f1ff0771ac4388ac634b99e67773))

* refactor: disambiguate note and prompt uuids ([`db5c457`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/db5c4570378fd7f50265b8ca3991cfb4dab7bbb5))

* refactor: clean up subdeck ([`7f03b42`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/7f03b42bdb46733683459d5b8e21df39e44bc427))

* refactor: misc. ([`8a366b3`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/8a366b3fc2dce6788ae93a5f80c0a57e40fc75b7))

* refactor: rename factory classes ([`af592f4`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/af592f4f51c4ed531582be5b7d538a27fd4680fb))

### Style

* style: linting ([`057d034`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/057d0348763f1c3b11dba4bd83877cbb65ac0831))

* style: linting ([`ba808b6`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/ba808b66ab4d83f919512cfce5d853d19714bdaa))

* style: final linting ([`8e59770`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/8e597700e268a2f26cc5dc940dfe1fb13789d0ab))

* style: linting ([`186208c`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/186208c9b009c211c66f57c1ce2efadf7ef2b909))

* style: linting ([`9f0d580`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/9f0d5802cc6155f2774faeeb293f72d72112a58d))

* style: linting ([`66e30e1`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/66e30e1b97e7ebed29b1552a0a48c659f09ffe9a))

### Unknown

* Merge pull request #25 from MartinBernstorff/martbern/rewrite

refactor: major rewrite ([`c37b743`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/c37b7434dae004b9c2bc35f9d5cee0f592122cd6))

* misc. ([`4459db1`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/4459db15a360d9eaa2251d6d9b423d09bf498708))

* misc. ([`86b5d19`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/86b5d19b2b1e9ce5a4980cc65b2e679a00cb7759))

* build. update deps ([`ca7a3dd`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/ca7a3dd63c173b12d200e887f979c8d7dd10e8bf))

* Merge branch &#39;main&#39; into martbern/rewrite ([`54b6416`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/54b64162ff9d06d3080464bb58e1987f4a4b68b7))

* cruft: add cruft ([`883da72`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/883da7222e64ab85a2fa39a829cd9f523b805cac))

* misc. ([`27883f5`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/27883f5f844537e353d7bfcca9921e1424f512e9))

* misc. ([`2337606`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/2337606135ad183ab49c150af860f4ba8c3a1385))

* misc. ([`4553e37`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/4553e37d141b752cf7bc4dd678c0a836c482ae4c))

* tests: first attempt at uid hash test ([`ddb65c4`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/ddb65c43b75514e52703c1e04949b53823b1d3ed))

* tests: simplify tests ([`8d6f096`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/8d6f096d79c9c1277e79a4113ed7ccc9d3adc351))

* tests: remove filepath requirement ([`8fd8095`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/8fd8095bc201ef44c627435b26b33404996a8186))

* tests: migrate old tests ([`c54fe52`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/c54fe521dacc90468dec6866fee8c6524c9c9558))

* misc. ([`aa2fc4e`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/aa2fc4e0bd4bf5e2f3eb1218d8af36c4ca381552))

* misc. changes ([`3f1a454`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/3f1a454ddf7385157ba465425256f5188a24e9dd))

* misc. ([`bcf2d2a`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/bcf2d2a2935611f8c7be9fe2cf26f31803efb347))

* init: add markdown based extractor ([`435dfef`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/435dfef5d5b587e6f6268af29f8b1cb5338d3cd4))

* Misc. additions ([`9679ef4`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/9679ef4fd6ad0f9e22cebf4592431ab4a4a74e2c))

* Add Anki launch and sync ([`76badd9`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/76badd9ba6106fe236aa2c0a00b6659fd6bf0529))

* Add wasabi ([`82ee3af`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/82ee3af163f856511a0000bd377fe44fd938c57a))

* Fix required space after A. ([`4348fa5`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/4348fa5607b20f81c7dcd51537bd351188f4a4e7))

* Merge branch &#39;main&#39; of https://github.com/martbern/personal-mnemonic-medium ([`8589b22`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/8589b226bcc979ea6cbbb98a96a90951ae5ab386))

* Update path ([`1621595`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/162159585d1efc7e6e42bac6da902e70ed8034da))

* Update requirements.txt ([`9137df8`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/9137df8a5d4dee2c1db58922d9b038ee7fa78bf3))

* Move to one file to avoid packaging ([`1b72c51`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/1b72c518a80cc7b58b0c95b8386ffc80cbf8aab2))

* Move all code to one file to avoid fighting with Python&#39;s packaging system ([`613aa41`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/613aa418134027eb0b4c74b5e0be1d6d238623d7))

* Merge branch &#39;main&#39; of https://github.com/martbern/personal-mnemonic-medium ([`bd94c55`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/bd94c55e0d3ab05cd782c30d7d8c7edd07a5419a))

* Fix file-structure to support pytest (closes #23) ([`2e2ccde`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/2e2ccde253f1f3cec6add993a258238d1b4ae6c0))

* Fix file-structure to support pytest (closes #23) ([`14b9976`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/14b99767f37294630df21871c7dd27834254118c))

* Add ankiconnect support (closes #21) ([`848dd09`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/848dd0925875d9349af21c968f322e26927c7de9))

* Hashes on md source (closes #19 and #20) ([`52af681`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/52af68150071c348970610513f01908e1078e10f))

* Merge branch &#39;main&#39; of https://github.com/martbern/personal-mnemonic-medium ([`72be9a8`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/72be9a8ab4ca21417da8165cdeb34c8abbb6ab86))

* Add test for multiline questions ([`d4c3d09`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/d4c3d09dd0447ad737b4509b32a8195f58e9778e))

* Update readme.md ([`33ec4e1`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/33ec4e14bdae031d8c58fcb75dae605784db88e5))

* Update readme.md ([`47ac665`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/47ac665daa186df19cb48ec9eca4eaf3db20fb1a))

* Create readme.md ([`6bb7264`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/6bb72641fa2a8476b197f8b4efe8bf03261a8eeb))

* Update python-app.yml ([`112713e`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/112713e769f53356d703bd980c25efcdc788521f))

* Merge branch &#39;main&#39; of https://github.com/martbern/personal-mnemonic-medium ([`9bdae6e`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/9bdae6eaab71b15078a5900d7396652dcc1875bf))

* Fix import for tests ([`9e2c787`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/9e2c787ec1dab2e47efc041f8b7dce1d3309e5c0))

* Update python-app.yml ([`26d4cc1`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/26d4cc14da8223303e9e755b0285d3e5ec67dece))

* Update python-app.yml ([`68402cc`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/68402ccea7ac97c59e0902a4dcb12b31ca31ddd4))

* Create python-app.yml ([`6a6bee4`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/6a6bee48f3710db24a33c66b04a355df692fbb64))

* Add tests to ensure stable card GUIDs (closes #17) ([`0349e55`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/0349e550bc8a86ce48991fb463f98ddfafb602f7))

* Update requirements with specific versions ([`3a7ccfd`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/3a7ccfd3f5e10c59a5be433686a0513dd518d3c0))

* Make hash more stable ([`3ea3240`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/3ea32400a09b9b9b696fe85016ca0586c6451a6a))

* Removes QA formatting from cards (closes #14) ([`858e1b1`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/858e1b13432ee0f185b4595483d1d88bf3f00341))

* Fix stripping of newlines (closes #4) ([`b80d7e6`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/b80d7e6e0c871c5067cd25e504ba2bec416b454e))

* Strip source before processing (closes #13) ([`a9649b8`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/a9649b871bb34eddfb2a77047148fdeee27ed383))

* Merge branch &#39;main&#39; of https://github.com/martbern/personal-mnemonic-medium ([`aa4fee1`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/aa4fee113f5385f4c91a61fd90bea26f2dde7937))

* Fix question containing newlines (#12) ([`b5b9066`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/b5b9066ae5210b2132d4d0756cb8e0beb96a649a))

* Fix question containing newlines (#12) ([`5717d0d`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/5717d0d344214d196641aa56fec641fcc5fcac73))

* Fix incorrect cloze card creation (closes #7) ([`65fbc50`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/65fbc500f85a034ce6dee23dc12e683dd9b599a2))

* Initial commit ([`74a00be`](https://github.com/MartinBernstorff/personal-mnemonic-medium/commit/74a00bed41d79bf6db49d66a4b3c3836cb0f6a36))
