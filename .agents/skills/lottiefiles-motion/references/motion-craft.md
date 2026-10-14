# Motion craft for Lottie Creator

Choose motion to communicate state or hierarchy, then tune the feel. Prefer a fast arrival with a slower settle, one deliberate overshoot, and small stagger between related layers. Use explicit peak and resting keyframes when a chosen easing cannot express the desired overshoot. Inspect the actual easing conventions and time units before applying curves.

For music, use the scene's actual FPS: frame = round(seconds × FPS). Place primary events on the agreed beat grid, but keep ambient breathing smooth and quiet. For unscored UI feedback, derive timing from the interaction rather than forcing a beat grid.

Keep approved artwork and colors. Group elements by their intended movement and name them before animating. Layer accents so the main action stays legible; avoid adding effects solely because the tool supports them. Check tiny-screen legibility and export/runtime support for blur, masks and shadows.

For a loop, check positional, opacity and velocity continuity at the seam. Test after export as well as in Creator. Build a static or shortened reduced-motion alternative and document how the app selects it.

For a targeted correction, re-read the actual layer IDs and keyframes, preserve the rest of the scene, and preview the changed interval. Never treat successful keyframe writes as proof of the intended visible motion.

Optional official motion guidance: https://github.com/LottieFiles/motion-design-skill (separate MIT-licensed package; retain its original attribution if installed).
