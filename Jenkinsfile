properties([
    buildDiscarder(logRotator(
        artifactDaysToKeepStr: '',
        artifactNumToKeepStr: '',
        daysToKeepStr: '30',
        numToKeepStr: '30'
    )),
    parameters([
        separator(name: 'separator-963609b8-ce70-45ab-8a61-ff6a77f51a4f'),
        choice(choices: ['master'], name: 'VERSION'),
        choice(choices: ['digator_opennlp'], name: 'BACKEND'),
        separator(name: 'separator-ae2bfb0c-1625-417a-b4a8-63cb19a81bb4')
    ])
])

k8s_build()
