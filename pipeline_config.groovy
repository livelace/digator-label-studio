libraries {
    dependency_check
    dependency_track {
        project = "digator-label-studio"
        version = "master"
    }
    git {
        repo_url = "https://github.com/livelace/digator-label-studio.git"
    }
    k8s_build
    kaniko {
        source = "digator_opennlp.dockerfile"
        destination = "data/digator-label-studio:digator_opennlp"
    }
    mattermost
    sonarqube
}
