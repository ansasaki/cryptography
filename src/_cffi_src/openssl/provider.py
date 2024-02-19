# This file is dual licensed under the terms of the Apache License, Version
# 2.0, and the BSD License. See the LICENSE file in the root of this repository
# for complete details.

from __future__ import annotations

INCLUDES = """
#if CRYPTOGRAPHY_OPENSSL_300_OR_GREATER
#include <openssl/provider.h>
#include <openssl/proverr.h>
#endif
"""

TYPES = """
static const long Cryptography_HAS_PROVIDERS;

typedef ... OSSL_PROVIDER;
typedef ... OSSL_LIB_CTX;
"""

FUNCTIONS = """
OSSL_PROVIDER *OSSL_PROVIDER_load(OSSL_LIB_CTX *, const char *);
int OSSL_PROVIDER_unload(OSSL_PROVIDER *prov);
"""

CUSTOMIZATIONS = """
#if CRYPTOGRAPHY_OPENSSL_300_OR_GREATER
static const long Cryptography_HAS_PROVIDERS = 1;
#else
static const long Cryptography_HAS_PROVIDERS = 0;
typedef void OSSL_PROVIDER;
typedef void OSSL_LIB_CTX;
OSSL_PROVIDER *(*OSSL_PROVIDER_load)(OSSL_LIB_CTX *, const char *) = NULL;
int (*OSSL_PROVIDER_unload)(OSSL_PROVIDER *) = NULL;
#endif
"""
