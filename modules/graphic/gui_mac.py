import Quartz.CoreGraphics as cg


class _MacAdapter:

    def capture(self, region=None):
        """region should be a CGRect, something like:

        >>> import Quartz.CoreGraphics as cg
        >>> region = cg.CGRectMake(0, 0, 100, 100)
        >>> sp = _MacAdapter()
        >>> sp.capture(region=region)

        The default region is CG.CGRectInfinite (captures the full screen)
        """

        if region is None:
            region = cg.CGRectInfinite
        else:
            if not isinstance(region, (list, tuple)):
                raise AttributeError("Capture region must be a list or tuple")
            if region[0] % 2 > 0:
                raise ValueError("Capture region width should be even (was %s)" % region[0])
            region = cg.CGRectMake(0, 0, region[0], region[1])

        image = cg.CGWindowListCreateImage(region, cg.kCGWindowListOptionOnScreenOnly, cg.kCGNullWindowID,
                                           cg.kCGWindowImageDefault)

        width = cg.CGImageGetWidth(image)
        height = cg.CGImageGetHeight(image)
        provider = cg.CGImageGetDataProvider(image)
        data = cg.CGDataProviderCopyData(provider)

        return data, width, height
