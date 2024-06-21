module.exports = {
  preset: 'ts-jest',
  testEnvironment: 'jsdom',
  moduleNameMapper: {
    '\\.(css|less|sass|scss)$': 'identity-obj-proxy',
    '^@/(.*)$': '<rootDir>/src/$1',
    '(react-markdown|rehype-raw|remark-gfm|react-syntax-highlighter/.*$)':
      '<rootDir>/src/__tests__/__mocks__/markdownMock.tsx',
  },
  transform: {
    '^.+\\.(ts|tsx)$': [
      'ts-jest',
      {
        tsconfig: {
          jsx: 'react-jsx',
        },
      },
    ],
    '^.+\\.(js|jsx)$': ['babel-jest', { presets: ['next/babel'] }],
  },
  extensionsToTreatAsEsm: ['.tsx'],
  testMatch: ['**/src/__tests__/**/*.test.ts?(x)'],
  collectCoverage: true,
  collectCoverageFrom: ['src/**/*.tsx'],
  coverageThreshold: {
    global: {
      statements: 80,
      branches: 40,
      functions: 80,
      lines: 80,
    },
  },
}
