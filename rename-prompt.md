You are a naming assistant. Given a list of file paths and minimal context from a static website, suggest a new filename (basename only, same extension) for each file. Rules:
- Lowercase, kebab-case, no spaces. SEO-friendly and human-readable.
- For HTML: use page purpose (e.g. about-us.html, contact.html). Keep index.html as index.html.
- For CSS/JS: use purpose (e.g. main-styles.css, analytics.js).
- For images: use content (e.g. logo-infygate.webp, hero-banner.webp). Use alt/title when provided.
- Return a JSON object: keys = exact original path strings, values = new basename only (e.g. "main.css"). Preserve extension.
- Do not change path prefix (e.g. css/ stays css/ by returning "name.css" not "css/name.css").

Files and context:
[
  {
    "path": "404.html",
    "context": {
      "title": "",
      "first_heading": "404"
    }
  },
  {
    "path": "about.html",
    "context": {
      "title": "Anil Industries | About Us",
      "first_heading": "YOUR PREFERRED STEEL SUPPLIERS"
    }
  },
  {
    "path": "coled-rolled-steel-strips.html",
    "context": {
      "title": "Anil Industries | Cold Rolled Steel Strips",
      "first_heading": "Cold Rolled Steel Strips"
    }
  },
  {
    "path": "contact.html",
    "context": {
      "title": "Anil Industries | Contact Us",
      "first_heading": "Contact Us"
    }
  },
  {
    "path": "css/559e64bf161e61fa0aca6e864c78191d.css",
    "context": {
      "path": "css/559e64bf161e61fa0aca6e864c78191d.css"
    }
  },
  {
    "path": "css/84d4a0216f16f715d9b301db3a8da352.css",
    "context": {
      "path": "css/84d4a0216f16f715d9b301db3a8da352.css"
    }
  },
  {
    "path": "css/99c4e6f40ee9111eea53b6472f3e60f9.css",
    "context": {
      "path": "css/99c4e6f40ee9111eea53b6472f3e60f9.css"
    }
  },
  {
    "path": "css/aae605bc4baaa28212332e2de6958423.css",
    "context": {
      "path": "css/aae605bc4baaa28212332e2de6958423.css"
    }
  },
  {
    "path": "css/c363a15baf9b3719c1570c22b012b369.css",
    "context": {
      "path": "css/c363a15baf9b3719c1570c22b012b369.css"
    }
  },
  {
    "path": "css/d09d646f062b67daeff66ff1410b63fc.css",
    "context": {
      "path": "css/d09d646f062b67daeff66ff1410b63fc.css"
    }
  },
  {
    "path": "css/internal-styles.css",
    "context": {
      "path": "css/internal-styles.css"
    }
  },
  {
    "path": "hardened-tempered-steel.html",
    "context": {
      "title": "Anil Industries | Hardened And Tempered Steel",
      "first_heading": "Hardened And Tempered Steel"
    }
  },
  {
    "path": "imgs/0a427c34198e76c22b71e6f4a0a4fdef.webp",
    "context": {
      "refs": [
        {
          "alt": "image description",
          "title": ""
        }
      ]
    }
  },
  {
    "path": "imgs/1320224f16ef823d7485d94d1fbe5095.webp",
    "context": {
      "refs": [
        {
          "alt": "",
          "title": ""
        }
      ]
    }
  },
  {
    "path": "imgs/1ef209328540ddeeddbc6a1e20556055.webp",
    "context": {
      "refs": [
        {
          "alt": "",
          "title": ""
        }
      ]
    }
  },
  {
    "path": "imgs/2fc0923de76d4bf3ae1f8879348002f2.webp",
    "context": {
      "refs": [
        {
          "alt": "",
          "title": ""
        }
      ]
    }
  },
  {
    "path": "imgs/3b116f54f921f867ca0692fe887c2b63.webp",
    "context": {
      "refs": [
        {
          "alt": "Vision",
          "title": ""
        }
      ]
    }
  },
  {
    "path": "imgs/85b7bd6425a8181f0c1c534546483da8.webp",
    "context": {
      "refs": [
        {
          "alt": "",
          "title": ""
        },
        {
          "alt": "",
          "title": ""
        }
      ]
    }
  },
  {
    "path": "imgs/8a77b717a01d2136d515b4a2c50511e1.webp",
    "context": {
      "refs": [
        {
          "alt": "Mission",
          "title": ""
        }
      ]
    }
  },
  {
    "path": "imgs/916313669540039e401049e898666b42.webp",
    "context": {
      "refs": [
        {
          "alt": "",
          "title": ""
        }
      ]
    }
  },
  {
    "path": "imgs/9344489a309f92818f0d6bc3180667bc.webp",
    "context": {
      "refs": [
        {
          "alt": "",
          "title": ""
        },
        {
          "alt": "",
          "title": ""
        }
      ]
    }
  },
  {
    "path": "imgs/95c50a8b8ba73faace0c46f0c9b31fb8.webp",
    "context": {
      "refs": [
        {
          "alt": "Our Quality",
          "title": ""
        },
        {
          "alt": "",
          "title": ""
        }
      ]
    }
  },
  {
    "path": "imgs/99255eac3bf5886d358856c76a2a9cb5.webp",
    "context": {
      "refs": [
        {
          "alt": "",
          "title": ""
        }
      ]
    }
  },
  {
    "path": "imgs/997325cd36e554b26f2d154bba0193bb.webp",
    "context": {
      "refs": [
        {
          "alt": "Our Products",
          "title": ""
        },
        {
          "alt": "",
          "title": ""
        }
      ]
    }
  },
  {
    "path": "imgs/9acb3029c2cf7c8ebfe203d6d496307e.webp",
    "context": {
      "refs": []
    }
  },
  {
    "path": "imgs/b5e614cae79fa443a39334bac6fc54cd.webp",
    "context": {
      "refs": [
        {
          "alt": "COLD ROLLED STEEL STRIPS",
          "title": ""
        }
      ]
    }
  },
  {
    "path": "imgs/b6c5337c2ee04f94e0c80f17fe59640d.webp",
    "context": {
      "refs": [
        {
          "alt": "",
          "title": ""
        },
        {
          "alt": "",
          "title": ""
        }
      ]
    }
  },
  {
    "path": "imgs/d696705989b29db5ddd051d3f2403d56.webp",
    "context": {
      "refs": [
        {
          "alt": "HARDENED AND TEMPERED STEEL",
          "title": ""
        }
      ]
    }
  },
  {
    "path": "imgs/ec5d784d7a5d8cb39f3881dfa133ac37.webp",
    "context": {
      "refs": [
        {
          "alt": "logo",
          "title": ""
        },
        {
          "alt": "logo",
          "title": ""
        },
        {
          "alt": "logo",
          "title": ""
        },
        {
          "alt": "logo",
          "title": ""
        },
        {
          "alt": "logo",
          "title": ""
        },
        {
          "alt": "logo",
          "title": ""
        }
      ]
    }
  },
  {
    "path": "imgs/f042471f5c7b5128a31ff282e66ab1d1.webp",
    "context": {
      "refs": [
        {
          "alt": "",
          "title": ""
        }
      ]
    }
  },
  {
    "path": "index.html",
    "context": {
      "title": "Anil Industries | Home",
      "first_heading": "Welcome to Anil Industries"
    }
  },
  {
    "path": "js/03b2eaae6007054a68c38e495f894dba.js",
    "context": {
      "path": "js/03b2eaae6007054a68c38e495f894dba.js"
    }
  },
  {
    "path": "js/0a105d712b6a6c836c48dd97d0f0cac1.js",
    "context": {
      "path": "js/0a105d712b6a6c836c48dd97d0f0cac1.js"
    }
  },
  {
    "path": "js/0c46896987137b0016246f6bc2243099.js",
    "context": {
      "path": "js/0c46896987137b0016246f6bc2243099.js"
    }
  },
  {
    "path": "js/165d7b0ddfa33362140feea997351b77.js",
    "context": {
      "path": "js/165d7b0ddfa33362140feea997351b77.js"
    }
  },
  {
    "path": "js/16df9ef05001a1741857bf99f5a5738f.js",
    "context": {
      "path": "js/16df9ef05001a1741857bf99f5a5738f.js"
    }
  },
  {
    "path": "js/2a85c11e395a8380b5915443e926b569.js",
    "context": {
      "path": "js/2a85c11e395a8380b5915443e926b569.js"
    }
  },
  {
    "path": "js/34be5330971fdbd18985525bd994b0aa.js",
    "context": {
      "path": "js/34be5330971fdbd18985525bd994b0aa.js"
    }
  },
  {
    "path": "js/35c5f9e096d4da33d2a62031daf14248.js",
    "context": {
      "path": "js/35c5f9e096d4da33d2a62031daf14248.js"
    }
  },
  {
    "path": "js/3d70953a848219e749fedc2cdb906675.js",
    "context": {
      "path": "js/3d70953a848219e749fedc2cdb906675.js"
    }
  },
  {
    "path": "js/3e940a33e44b65c1c0af8bb80a893530.js",
    "context": {
      "path": "js/3e940a33e44b65c1c0af8bb80a893530.js"
    }
  },
  {
    "path": "js/544d012df7acf9c3f0920f67c9e322b9.js",
    "context": {
      "path": "js/544d012df7acf9c3f0920f67c9e322b9.js"
    }
  },
  {
    "path": "js/57d119d998d518b01f9d5ccb5e4d4c52.js",
    "context": {
      "path": "js/57d119d998d518b01f9d5ccb5e4d4c52.js"
    }
  },
  {
    "path": "js/67f6e2f99c3c3133e0dc669919fff5c5.js",
    "context": {
      "path": "js/67f6e2f99c3c3133e0dc669919fff5c5.js"
    }
  },
  {
    "path": "js/7045b35c5bd0e9c7cf59f1900eeeec41.js",
    "context": {
      "path": "js/7045b35c5bd0e9c7cf59f1900eeeec41.js"
    }
  },
  {
    "path": "js/7260bab328b0ad74815a5efb377bcc67.js",
    "context": {
      "path": "js/7260bab328b0ad74815a5efb377bcc67.js"
    }
  },
  {
    "path": "js/893de96f1b6da546bd7c814964723eca.js",
    "context": {
      "path": "js/893de96f1b6da546bd7c814964723eca.js"
    }
  },
  {
    "path": "js/93e29fe348ddc9b71aba9c842adc18b8.js",
    "context": {
      "path": "js/93e29fe348ddc9b71aba9c842adc18b8.js"
    }
  },
  {
    "path": "js/9455859483e31e4da0e28f10d0742c2a.js",
    "context": {
      "path": "js/9455859483e31e4da0e28f10d0742c2a.js"
    }
  },
  {
    "path": "js/9db10375d298678e53777a2347b87073.js",
    "context": {
      "path": "js/9db10375d298678e53777a2347b87073.js"
    }
  },
  {
    "path": "js/9f9b6e54f82a6bbc8bac9b89327024bc.js",
    "context": {
      "path": "js/9f9b6e54f82a6bbc8bac9b89327024bc.js"
    }
  },
  {
    "path": "js/a2261649751fa61b606222c9b2ea3b80.js",
    "context": {
      "path": "js/a2261649751fa61b606222c9b2ea3b80.js"
    }
  },
  {
    "path": "js/b0bade6d42c2702ca85774296cc507c4.js",
    "context": {
      "path": "js/b0bade6d42c2702ca85774296cc507c4.js"
    }
  },
  {
    "path": "js/cd1ed86c1e7f06d985fd71bc10bd4b04.js",
    "context": {
      "path": "js/cd1ed86c1e7f06d985fd71bc10bd4b04.js"
    }
  },
  {
    "path": "js/cecb447a04bbe3e8982190dd6e697120.js",
    "context": {
      "path": "js/cecb447a04bbe3e8982190dd6e697120.js"
    }
  },
  {
    "path": "js/d80b370d82680fc786dcc943a327b9f2.js",
    "context": {
      "path": "js/d80b370d82680fc786dcc943a327b9f2.js"
    }
  },
  {
    "path": "js/df80c5cbcb312a9c7c0b2ebb6ac5f592.js",
    "context": {
      "path": "js/df80c5cbcb312a9c7c0b2ebb6ac5f592.js"
    }
  },
  {
    "path": "js/f1e5dbc1ece900d164c2e9aa2d6a1386.js",
    "context": {
      "path": "js/f1e5dbc1ece900d164c2e9aa2d6a1386.js"
    }
  },
  {
    "path": "js/f3f02c438592c8e1bbe551f4dbbf4f5c.js",
    "context": {
      "path": "js/f3f02c438592c8e1bbe551f4dbbf4f5c.js"
    }
  },
  {
    "path": "js/faf9ce4e848522206b5c3043551fb2d7.js",
    "context": {
      "path": "js/faf9ce4e848522206b5c3043551fb2d7.js"
    }
  },
  {
    "path": "qualities.html",
    "context": {
      "title": "Anil Industries | Manufacturing",
      "first_heading": "WORLD CLASS MANUFACTURING BASE"
    }
  }
]

Return only a JSON object mapping each path to its new basename (same extension). No other text.