class Solution(object):
    def licenseKeyFormatting(self, S, K):
        S = S.replace('-','').upper()
        r = len(S) % K
        pattern = re.compile(r'[A-Z0-9]{%d}' % K)
        matched = re.findall(pattern, S[r:])
        if not r:
            return "-".join(matched)
        return "-".join([S[:r]] + matched)
