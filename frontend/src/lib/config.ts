// Environment mode types
export enum EnvMode {
  LOCAL = 'local',
  STAGING = 'staging',
  PRODUCTION = 'production',
}

// Subscription tier structure
export interface SubscriptionTierData {
  priceId: string;
  name: string;
}

// Subscription tiers structure
export interface SubscriptionTiers {
  SPARK: SubscriptionTierData;
  BOOST: SubscriptionTierData;
  ASCEND: SubscriptionTierData;
  PRO: SubscriptionTierData;
  ELITE: SubscriptionTierData;
  ULTIMATE: SubscriptionTierData;
  ENTERPRISE: SubscriptionTierData;
}

// Configuration object
interface Config {
  ENV_MODE: EnvMode;
  IS_LOCAL: boolean;
  SUBSCRIPTION_TIERS: SubscriptionTiers;
}

// Production tier IDs
const PROD_TIERS: SubscriptionTiers = {
  SPARK: {
    priceId: 'price_1RbMFsJ07oA1wY5pn9qujLZK',
    name: 'Spark',
  },
  BOOST: {
    priceId: 'price_1RbMG3J07oA1wY5p3HpVIPyq',
    name: 'Boost',
  },
  ASCEND: {
    priceId: 'price_1RbMG9J07oA1wY5pfLic42hS',
    name: 'Ascend',
  },
  PRO: {
    priceId: 'price_1RbMGLJ07oA1wY5pHEGapf1X',
    name: 'Pro',
  },
  ELITE: {
    priceId: 'price_1RbMGRJ07oA1wY5pECiIJMck',
    name: 'Elite',
  },
  ULTIMATE: {
    priceId: 'price_1RbMGXJ07oA1wY5pWyyWRie1',
    name: 'Ultimate',
  },
  ENTERPRISE: {
    priceId: 'price_1RbMGcJ07oA1wY5pVy0yBgnl',
    name: 'Enterprise',
  },
} as const;

// Staging tier IDs
const STAGING_TIERS: SubscriptionTiers = {
  SPARK: {
    priceId: 'price_1RbMFsJ07oA1wY5pn9qujLZK',
    name: 'Spark',
  },
  BOOST: {
    priceId: 'price_1RbMG3J07oA1wY5p3HpVIPyq',
    name: 'Boost',
  },
  ASCEND: {
    priceId: 'price_1RbMG9J07oA1wY5pfLic42hS',
    name: 'Ascend',
  },
  PRO: {
    priceId: 'price_1RbMGLJ07oA1wY5pHEGapf1X',
    name: 'Pro',
  },
  ELITE: {
    priceId: 'price_1RbMGRJ07oA1wY5pECiIJMck',
    name: 'Elite',
  },
  ULTIMATE: {
    priceId: 'price_1RbMGXJ07oA1wY5pWyyWRie1',
    name: 'Ultimate',
  },
  ENTERPRISE: {
    priceId: 'price_1RbMGcJ07oA1wY5pVy0yBgnl',
    name: 'Enterprise',
  },
} as const;

// Determine the environment mode from environment variables
const getEnvironmentMode = (): EnvMode => {
  // Get the environment mode from the environment variable, if set
  const envMode = process.env.NEXT_PUBLIC_ENV_MODE?.toLowerCase();

  // First check if the environment variable is explicitly set
  if (envMode) {
    if (envMode === EnvMode.LOCAL) {
      console.log('Using explicitly set LOCAL environment mode');
      return EnvMode.LOCAL;
    } else if (envMode === EnvMode.STAGING) {
      console.log('Using explicitly set STAGING environment mode');
      return EnvMode.STAGING;
    } else if (envMode === EnvMode.PRODUCTION) {
      console.log('Using explicitly set PRODUCTION environment mode');
      return EnvMode.PRODUCTION;
    }
  }

  // If no valid environment mode is set, fall back to defaults based on NODE_ENV
  if (process.env.NODE_ENV === 'development') {
    console.log('Defaulting to LOCAL environment mode in development');
    return EnvMode.LOCAL;
  } else {
    console.log('Defaulting to PRODUCTION environment mode');
    return EnvMode.PRODUCTION;
  }
};

// Get the environment mode once to ensure consistency
const currentEnvMode = getEnvironmentMode();

// Create the config object
export const config: Config = {
  ENV_MODE: currentEnvMode,
  IS_LOCAL: currentEnvMode === EnvMode.LOCAL,
  SUBSCRIPTION_TIERS:
    currentEnvMode === EnvMode.STAGING ? STAGING_TIERS : PROD_TIERS,
};

// Helper function to check if we're in local mode (for component conditionals)
export const isLocalMode = (): boolean => {
  return config.IS_LOCAL;
};

// Export subscription tier type for typing elsewhere
export type SubscriptionTier = keyof typeof PROD_TIERS;
