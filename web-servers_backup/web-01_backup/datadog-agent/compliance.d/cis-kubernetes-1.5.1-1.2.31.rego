package datadog

valid_process(process) {
	process.flags["--client-ca-file"] != ""
}
