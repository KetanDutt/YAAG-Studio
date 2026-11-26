# Unslop adaptation and attribution

This project's design review methodology is adapted from **Unslop**, created by Damir Sokolovsky (@heydamir): https://github.com/heydamir/unslop

Unslop is licensed under **Creative Commons Attribution 4.0 International (CC BY 4.0)**. Attribution: Damir Sokolovsky, “Unslop,” https://github.com/heydamir/unslop, CC BY 4.0. This file records the attribution for this adaptation.

The source's useful process—inspect the real product, name specific visual problems, derive a direction from the product, refine in deliberate passes, and check the result—was applied to YAAG Studio. The source skill itself and its screenshots/examples are not copied into this project. The implementation choices here are original to YAAG Studio and its user-provided wall-calendar reference.

## Adapted principles

- Keep existing calendar functionality and content; refine the actual product instead of replacing it with a mockup.
- Let the generated calendar be the meaningful visual moment; keep navigation and controls quiet.
- Use an editorial print-studio world (paper, ink, fine rules, botanical green) rather than generic SaaS decoration.
- Apply translucent blur only to the functional top toolbar, with a high-opacity fallback. Keep the paper/date content opaque and printable.
- Use a product-specific calendar-grid mark rather than a generic decorative symbol.
- Apply responsive, typography, control, motion, and accessibility refinements without adding a framework or runtime dependency.

## Apple Liquid Glass inspiration

The implementation borrows only the broader idea of a distinct, translucent functional layer. It does not copy Apple's proprietary assets or exact interface. Apple's current materials guidance recommends keeping Liquid Glass in functional/navigation layers and using it sparingly; the calendar page remains a standard opaque content surface.

Apple Human Interface Guidelines, Materials: https://developer.apple.com/design/human-interface-guidelines/materials
Apple Human Interface Guidelines, Motion: https://developer.apple.com/design/human-interface-guidelines/motion
