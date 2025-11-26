package main

import "github.com/firefly-zero/firefly-go/firefly"

func init() {
	firefly.Boot = boot
	firefly.Update = update
	firefly.Render = render
}

func boot() {
	// BOOT
}

func update() {
	// UPDATE
}

func render() {
	// RENDER
}
