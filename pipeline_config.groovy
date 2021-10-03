def APP_NAME = "digator-label-studio"
def APP_REPO = "https://github.com/livelace/digator-label-studio.git"
def APP_VERSION = env.VERSION + '-${GIT_COMMIT_SHORT}'

libraries {
    dependency_check
    dependency_track {
        project = "${APP_NAME}"
        version = "env.VERSION"
    }
    git {
        repo_url = "${APP_REPO}"
        //repo_branch = env.VERSION
    }
    harbor_replicate {
        policy = "${APP_NAME}"
    }
    k8s_build
    kaniko {
        source = "${env.BACKEND}.dockerfile"
        destination = "data/${APP_NAME}:${env.BACKEND}"
    }
    mattermost
    python
    sonarqube
}
